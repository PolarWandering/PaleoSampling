import numpy as np

from .kappa import lat_correction, kappa_from_latitude, kappa2angular


def inverse(f, delta=1e-8):
    """
    Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta.
    """
    def f_1(y):
        low, high = 0, 10e7
        last, mid = 0, high/2
        while abs(mid-last) > delta:
            if f(mid) < y:
                low = mid
            else:
                high = mid
            last, mid = mid, (low + high)/2
        return mid
    return f_1

def rho_kappa(k, n):
    """
    Expected vector length of Fisher distribition
    """
    if n > 1:
        return 1/np.tanh(k) - 1/k
    else:
        return 1
    
    
def kappa_theoretical(params):
    """
    Theoretical result
    """
    
    N = params.N
    n = params.n0
    if params.secular_method == "G":
        k_between = kappa_from_latitude(params.site_lat, degrees=True)
    else:
        raise ValueError()
    k_within = params.kappa_within_site
    p = params.outlier_rate
    lat = params.site_lat
    
    if p > 0.001 and n > 2:
        rho_kappa_inverse = inverse(lambda x: rho_kappa(x, n=2))
        k_within = rho_kappa_inverse( (1-p) * rho_kappa(k_within, 2) )
    
    k_within_site = n * rho_kappa(k_within, n) * k_within 
    
    k_within_site_lat_corrected = k_within_site / lat_correction(lat, degrees=True)
    
    k_between_vgp = k_between 
    
    k_combined = k_within_site_lat_corrected * k_between_vgp / (k_within_site_lat_corrected + k_between_vgp)
    
    k_tot = N * k_combined * rho_kappa(k_combined, N) #* (1 - p)
        
    if n==1 and p > 0.001:
        rho_kappa_inverse = inverse(lambda x: rho_kappa(x, n=2))
        k_combined = rho_kappa_inverse( (1-p) * rho_kappa(k_combined, 2) )
        k_tot = N * k_combined * rho_kappa(k_combined, N)
        
    return float(k_tot)
        
    if p < 0.001:
        return float(k_tot)
    else:
        """
        Compute the expectation of k * \rho(k) when n0 ~ Binom(n, 1-p) and use that for the within dispersion
        """
        from scipy.stats import binom
        k_tot = 0
        for n0_ in range(n+1):
            k_within_site =  n0_ * k_within * rho_kappa(k_within, n0_)
        
            k_within_site_lat_corrected = k_within_site / lat_correction(lat, degrees=True)
    
            k_between_vgp = k_between 

            k_combined = k_within_site_lat_corrected * k_between_vgp / (k_within_site_lat_corrected + k_between_vgp)

            if k_combined > 0.0001:
                k_tot += binom(n=n, p=1-p).pmf(n0_) * ( N * k_combined * rho_kappa(k_combined, N) )
        
        return float(k_tot)
        
        rho_kappa_inverse = inverse(lambda x: rho_kappa(x, n=2))
        # _factor =  1 - p
        # _factor = 1 / np.sqrt(1 + p/(1-p))
        _factor = ( 1 + (1 - p) ** 2 ) / 2
        return rho_kappa_inverse( _factor * rho_kappa(k_tot, 2) )
