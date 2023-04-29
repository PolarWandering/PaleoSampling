import numpy as np

from .kappa import lat_correction, kappa_from_latitude, kappa2angular

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
        k0 = kappa_from_latitude(params.site_lat, degrees=True)
    else:
        raise ValueError()
    k1 = params.kappa_within_site
    p = params.outlier_rate
    lat = params.site_lat
    
    k1_corrected = k1 / lat_correction(lat, degrees=True)
    # print(k1, k1_corrected)
    # k1_corrected = k1
    _kappa =  N * k0 * rho_kappa(k0, N) / (1 + (k0)/(k1_corrected * rho_kappa(k1_corrected, n) * (1-p) * n))
    
    return _kappa
    # return float(kappa2angular(_kappa))