import numpy as np
import pandas as pd

import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag


def robust_fisher_mean(decs, incs):
    assert len(decs) == len(incs)
    if len(decs) == 1:
        return decs[0], incs[0]
    else:
        pole_mean = ipmag.fisher_mean(dec=decs, inc=incs)
        return pole_mean['dec'], pole_mean['inc']
    

def estimate_pole(df_sample, ignore_outliers=False, method='mean-of-means', kappa0=None, kappa1=None):
    '''
    Function to estimate the Fisher estimate for the paloemagnetic pole
    '''
    if ignore_outliers:
        df = df_sample[df_sample.is_outlier==0]
    else:
        df = df_sample
    
    L = len(np.unique(df.sample_site))
    df_site = df.groupby('sample_site').apply(lambda row : pd.Series({'declination': robust_fisher_mean(row.declination.values, row.inclination.values)[0],
                                                                      'inclination': robust_fisher_mean(row.declination.values, row.inclination.values)[1],
                                                                      'n_samples': len(row.declination.values)}))

    # Final fisher mean
    pole_estimate = ipmag.fisher_mean(dec=df_site.declination.values, inc=df_site.inclination.values)
 
    if method=='mean-of-means':
        return pole_estimate['dec'], pole_estimate['inc'], df_site.n_samples.sum()        
    
    elif method=='MLE-known-kappa':
        # we solve iterativelly starting from the estimate based on method='mean-of-means'
        Mu = np.zeros((K+1,3))
        # move all to cartesian coordinates 
        Mu[0,:] = pmag.dir2cart([pole_estimate['dec'], pole_estimate['inc']])
        # sort df_site
        df_site = df_site.sort_values(by=['sample_site'])
        Mu[1:,:] = pmag.dir2cart(df_site[['declination', 'inclination']].values)
        X = ...
        
        decired_tolerance = False
        while iter_max < 1000 and not decired_tolerance:
            for site in range(1, K+1):
                ### Add cartesian coordinates to the data 
                Mu[site,:] = kappa_1 *  + kappa_0 * Mu[0,:]
            # Normalize 
            iter_max += 1