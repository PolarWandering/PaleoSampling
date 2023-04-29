import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag

from typing import NamedTuple

# from .estimate import robust_fisher_mean, estimate_pole
from .kappa import *

class Params(NamedTuple):
    """
    Macro to encapsulate all the parameters in the sampling model.
    """

    # Number of sites
    N : int
    # Number of samples per site
    n0 : int
    
    # Concentration parameter within site
    kappa_within_site : float    

    # Latitude and longitude of site
    site_lat  : float 
    site_long : float

    # Proportion of outliers to be sampled from uniform distribution
    outlier_rate : float

    # Method to sample secular variation. Options are ("tk03", "G", "Fisher")
    secular_method : str 
    kappa_secular : float    # Just needed for Fisher sampler
    
    
def generate_design(params): 
    '''
    Given the number of possible samples to collect and how many samples do we 
    want per site, returns a list whose lenght is the number of sites and the repeated
    number of samples per site
    '''
    equal_template = np.repeat(params.n0, params.N)

    assert np.sum(equal_template) == params.N * params.n0
    assert np.min(equal_template) >= params.n0
    assert np.max(equal_template) <= params.n0
    return equal_template
        
    
def generate_samples(params):
    '''
    Fuction to generate experimental design 
    
    Arguments:
        - params 
    Returns:
        - List of number of samples needed to take per site
    '''
    
    design = generate_design(params)

    if params.secular_method=="tk03":
        directions_secular = ipmag.tk03(n=params.N.k, dec=0, lat=params.site_lat, rev='no', G1=-18e3, G2=0, G3=0, B_threshold=0)
        dec_secular, inc_secular = np.asarray(directions_secular)[:,0], np.asarray(directions_secular)[:,1]
    
    elif params.secular_method=="G" or params.secular_method=="Fisher":

        # Pick value of kappa used for Fisher sampling
        if params.secular_method=="G":
            _kappa_secular = float(kappa_from_latitude(params.site_lat, degrees=True))
        if params.secular_method=="Fisher":
            _kappa_secular = params.kappa_secular

        directional_secular = ipmag.fishrot(k=_kappa_secular, 
                                            n=params.N,
                                            dec=0,
                                            inc=90,
                                            di_block=True)

        # Transform to inclination, declination
        vgp_secular = np.apply_along_axis(lambda x: pmag.vgp_di(x[1], x[0], slat=params.site_lat, slong=params.site_long), axis=1, arr = directional_secular)
        dec_secular, inc_secular = vgp_secular[:,0], vgp_secular[:,1]
        
        assert np.min(inc_secular) > -90 and np.max(inc_secular) < 90, "Inclination must be [-90, 90]"

    else:
        raise ValueError("Method for sampling secular variation not implemented.")
        
    
    for i, nk in enumerate(design):
        """
        i is a counter representing the site number.
        nk is the number of samples in the i_th site
        """

        # Pick samples to be outliers
        outliers = np.random.binomial(1, params.outlier_rate, nk) 
        # Arrange the true samples and then the outliers
        outliers = sorted(outliers)
        
        n_outliers = np.sum(outliers)     # Number of outliers
        n_samples  = nk - n_outliers      # Number of real samples
        
        # Sample in-site observations
        declinations, inclinations = ipmag.fishrot(k=params.kappa_within_site, 
                                                   n=n_samples,
                                                   dec=dec_secular[i],
                                                   inc=inc_secular[i],
                                                   di_block=False)

        # Sample VGP outliers in (dec, inc) space
        vgp_dec_out, vgp_inc_out = pmag.get_unf(n_outliers).T
        
        samples_dec = np.hstack((declinations, vgp_dec_out))
        samples_inc = np.hstack((inclinations, vgp_inc_out))   

        samples_vgp = np.vstack((samples_dec, samples_inc)).T         

        # Convert specimen/sample/directions to VGP space
        samples_dia = np.apply_along_axis(lambda x: pmag.dia_vgp(x[0], x[1], 0, params.site_lat, params.site_long), axis=1, arr = samples_vgp)[:,:2]  
        
        # vgp_lon, vgp_lat = [], [] 
        # for j in range(len(vgp_dec)):
        #     lon, lat, _, _ = pmag.dia_vgp(vgp_dec[j], vgp_inc[j], 0, params.site_lat, params.site_lon)
        #     vgp_lon.append(lon)
        #     vgp_lat.append(lat)
        
        df_ = pd.DataFrame({'sample_site': i,
                            'vgp_long': samples_dia[:,0],
                            'vgp_lat': samples_dia[:,1],
                            'vgp_dec': samples_dec,
                            'vgp_inc': samples_inc,
                            'is_outlier': outliers})
        if i==0:
            df = df_
        else:
            df = pd.concat([df, df_], axis=0, ignore_index=True)
            
    return df
