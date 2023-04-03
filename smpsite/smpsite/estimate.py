import numpy as np
import pandas as pd

import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag

from .sampling import generate_samples

def robust_fisher_mean(decs, incs):
    assert len(decs) == len(incs)
    if len(decs) == 1:
        return decs[0], incs[0]
    else:
        pole_mean = ipmag.fisher_mean(dec=decs, inc=incs)
        return pole_mean['dec'], pole_mean['inc']
    

def estimate_pole(df_sample, params, ignore_outliers=False, method='mean-of-means', kappa0=None, kappa1=None):
    '''
    Function to estimate the Fisher estimate for the paloemagnetic pole
    Returns:
     - Pole coordinates
     - Number of samples (total)
     - Number of samples per site.
    '''
    if ignore_outliers:
        df = df_sample[df_sample.is_outlier==0]
    else:
        df = df_sample
    
    L = len(np.unique(df.sample_site))

    
    # Note: Add kappa and csd to the output, then we can sample from these distributions and compare with the MLEstimate
    df_site = df.groupby('sample_site').apply(lambda row : pd.Series({'vgp_dec': robust_fisher_mean(row.vgp_dec.values, row.vgp_inc.values)[0],
                                                                      'vgp_inc': robust_fisher_mean(row.vgp_dec.values, row.vgp_inc.values)[1],
                                                                      'n_samples': len(row.vgp_dec.values)}))
    
    # Now we need to move this to (lat, lon) space. 
    vgp_long, vgp_lat, _, _ = pmag.dia_vgp(df_site.vgp_dec, 
                                           df_site.vgp_inc, 
                                           0, 
                                           params.site_lat, 
                                           params.site_long)
 
    df_site["vgp_long"] = vgp_long
    df_site["vgp_lat"]  = vgp_lat

    # Final fisher mean
    pole_estimate = ipmag.fisher_mean(dec=df_site.vgp_long.values, 
                                      inc=df_site.vgp_lat.values)
 

    return pole_estimate['dec'], pole_estimate['inc'], df_site.n_samples.sum(), df_site.n_samples.unique()           
    

            
def simulate_estimations(params, n_iters=100, ignore_outliers=False, seed=None):
    '''
    Given a sampling strategy (samples per site and total number of samples)
    returns a DF with results of n_iters simulated poles.
    '''
    
    poles = {'plong':[], 'plat':[], 'total_samples':[], 'samples_per_sites':[] }
    
    if seed is not None:
        np.random.seed(seed)
    
    for _ in range(n_iters):

        df_sample = generate_samples(params)
        
        # estimate_pole() first groups samples by # of site and then computes a fisher mean for the pole (means of means)
        pole_long, pole_lat, total_samples, samples_per_site = estimate_pole(df_sample, params, ignore_outliers=ignore_outliers)
        
        poles['plong'].append(pole_long)
        poles['plat'].append(pole_lat)
        poles['total_samples'].append(total_samples)
        poles['samples_per_sites'].append( samples_per_site)

    df_poles = pd.DataFrame(poles)
    df_poles['error_angle'] = 90.0 - df_poles.plat
    
    return df_poles