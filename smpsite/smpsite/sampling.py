import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag

from typing import NamedTuple

from .estimate import robust_fisher_mean, estimate_pole

class Params(NamedTuple):
    
    kappa_vgp : float    
    kappa_secular : float 
    outlier_rate : float
    N_per_site: int
    N : int
    site_lat : float
    site_long : float
    
    
def generate_design(params): 
    
    equal_template = np.array([params.N_per_site] * int(params.N/params.N_per_site))
    equal_template[:params.N % params.N_per_site] += 1
    assert np.sum(equal_template) == params.N, 'this happens because there is no way of keeping the right sampling'
    assert np.min(equal_template) >= params.N_per_site
    assert np.max(equal_template) <= params.N_per_site+1
    return equal_template
    
    
    
def generate_samples(params):
    '''
    Fuction to generate experimental design 
    
    Arguments:
        - n: total number of samples we are able to recollect
        - n_site: number of samples per site (fixed and constant for all sites for now)
        - p: value between [0,1] representing the probabilty of outlier. 
    Returns:
        - List of number of samples needed to take per site
    '''
    
    design = generate_design(params)
    N_sites = len(design)
    
    # sample secular variations
    # lat, lon
    # here is where I can replace by TK03 model
    secular_declinations, secular_inclinations = ipmag.fishrot(k=params.kappa_secular,
                                                               n=N_sites, 
                                                               dec=0, 
                                                               inc=90, 
                                                               di_block=False)
    
    for i, nk in enumerate(design):
        outliers = np.random.binomial(1, params.outlier_rate, nk)
        outliers = sorted(outliers)
        n_outliers = np.sum(outliers)
        n_samples = nk - n_outliers
        
        # Transform VGP coordinates to directions (D, I) coordinates 
        # inc, dec
        dec_vgp, inc_vgp = pmag.vgp_di(plat=secular_inclinations[i], 
                                       plong=secular_declinations[i], 
                                       slat=params.site_lat, 
                                       slong=params.site_long)

    
        # Sample real samples (within-site)
        declinations, inclinations = ipmag.fishrot(k=params.kappa_vgp, 
                                                   n=n_samples,
                                                   dec=dec_vgp,
                                                   inc=inc_vgp,
                                                   di_block=False)

        # Convert specimenst to geographical space
        for j in range(len(declinations)):
            trans_dec, trans_inc, _, _ = pmag.dia_vgp(declinations[j], inclinations[j], 0, params.site_lat, params.site_long)
            declinations[j] = trans_dec
            inclinations[j] = trans_inc
        
        # Sample outliers 
        declinations_out, inclinations_out = pmag.get_unf(n_outliers).T
        
        declinations = np.concatenate((declinations, declinations_out))
        inclinations = np.concatenate((inclinations, inclinations_out))
        
        df_ = pd.DataFrame({'sample_site': i,
                            'declination': declinations,
                            'inclination': inclinations,
                            'is_outlier': outliers})
        if i==0:
            df = df_
        else:
            df = pd.concat([df, df_], axis=0, ignore_index=True)
            
    return df



def simulate_estimations(params, n_iters=100, ignore_outliers=False, seed=None):

    poles_dec, poles_inc, all_total_samples = [], [], []

    if seed is not None:
        np.random.seed(seed)
    
    for _ in range(n_iters):

        df_sample = generate_samples(params)
        pole_dec, pole_inc, total_samples = estimate_pole(df_sample, ignore_outliers=ignore_outliers)
        poles_dec.append(pole_dec)
        poles_inc.append(pole_inc)
        all_total_samples.append(total_samples)

    df_poles = pd.DataFrame({'declination': poles_dec, 
                             'inclination': poles_inc, 
                             'total_samples': all_total_samples})
    df_poles['error_angle'] = 90.0 - df_poles.inclination
    
    return df_poles