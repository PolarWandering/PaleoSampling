import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag

from typing import NamedTuple

# from .estimate import robust_fisher_mean, estimate_pole


class Params(NamedTuple):
    
    kappa_within_site : float    
    site_lat : float # Governing parameter of the concentration
    outlier_rate : float
    n : int # number of sites 
    k : int # number of samples per site 
    site_lon : float

    
def generate_design(params): 
    '''
    Given the number of possible samples to collect and how many samples do we 
    want per site, returns a list whose lenght is the number of sites and the repeated
    number of samples per site
    '''
    equal_template = np.repeat(params.k, params.n)
    # equal_template = np.array([params.N_per_site] * int(params.N/params.N_per_site))
    # equal_template[:params.N % params.N_per_site] += 1
    assert np.sum(equal_template) == params.n * params.k
    assert np.min(equal_template) >= params.k
    assert np.max(equal_template) <= params.k
    return equal_template
        
    
def generate_samples(params, secular_method="tk03"):
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
    latitude = params.site_lat
    
    # Sample directions from secular variation model 
    if secular_method=="tk03":
        directions_secular = ipmag.tk03(n=N_sites, dec=0, lat=latitude, rev='no', G1=-18e3, G2=0, G3=0, B_threshold=0)
        dec_secular, inc_secular = np.asarray(directions_secular)[:,0], np.asarray(directions_secular)[:,1]
    elif secular_method=="Fisher":
        longitude_secular, latitude_secular = ipmag.fishrot(k=50, 
                                                            n=N_sites,
                                                            dec=0,
                                                            inc=90,
                                                            di_block=False)
        # Transform to inclination, declination
        #
        # dec_secular, inc_secular = ...
    else:
        raise ValueError("Method for sampling secular variation not implemented.")
        
    
    for i, nk in enumerate(design):
        
        ''' i is a counter representing the site number.
            nk is the number of samples in the i_th site
        '''
        outliers = np.random.binomial(1, params.outlier_rate, nk) # probability of outliers 
        
        # Arrange the true samples and then the outliers
        outliers = sorted(outliers)
        
        n_outliers = np.sum(outliers)
        n_samples = nk - n_outliers
        
        # Sample in-site observations
        declinations, inclinations = ipmag.fishrot(k=params.kappa_within_site, 
                                                   n=n_samples,
                                                   dec=dec_secular[i],
                                                   inc=inc_secular[i],
                                                   di_block=False)

        # Sample VGP outliers in (dec, inc) space
        vgp_dec_out, vgp_inc_out = pmag.get_unf(n_outliers).T
        
        vgp_dec = np.hstack((declinations, vgp_dec_out))
        vgp_inc = np.hstack((inclinations, vgp_inc_out))   
                
        # Convert specimen/sample/directions to VGP space
        vgp_lon, vgp_lat = [], [] 
        for j in range(len(vgp_dec)):
            lon, lat, _, _ = pmag.dia_vgp(vgp_dec[j], vgp_inc[j], 0, params.site_lat, params.site_lon)
            vgp_lon.append(lon)
            vgp_lat.append(lat)
        
        df_ = pd.DataFrame({'sample_site': i,
                            'vgp_lon': vgp_lon,
                            'vgp_lat': vgp_lat,
                            'vgp_dec': vgp_dec,
                            'vgp_inc': vgp_inc,
                            'is_outlier': outliers})
        if i==0:
            df = df_
        else:
            df = pd.concat([df, df_], axis=0, ignore_index=True)
            
    return df
