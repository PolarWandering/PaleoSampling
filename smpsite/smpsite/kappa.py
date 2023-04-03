import numpy as np
import pandas as pd
from scipy import interpolate

df = pd.read_csv("smpsite/smpsite/kappa_tabular/kappa2angular.csv", header=0)

kappa2angular = interpolate.interp1d(df.kappa, df.std_angular)
angular2kappa = interpolate.interp1d(df.std_angular, df.kappa)



def kappa_from_latitude(latitude, a = 11.23, b=0.27, degrees = False, inversion="interpolation"):
    """
    Input: given a latitude (in radians), and the $a$ and $b$ parameters that best describes the Model G that we want to simulate, 
    it returns the theoretical concentration parameter (kappa) that a sample of VGPs would have at any given latitude.
    Notes: 
     - we use a power-law fit to find an empirical relation between kappa and angular dispersion (found to be $ S = 72.33 \kappa^-0.50 $)
     - The default $a$ and $b$ values are from Doubrovine et al., (2019) (for the last 10 Ma - PSV10)
    """
    
    if degrees == False: 
        latitude = np.degrees(np.abs(latitude))
        
    # Model G from Doubrovine et al. 2019  
    S = np.sqrt( a ** 2 + ( latitude *b ) ** 2 ) 
    
    if inversion == "power-law":
        return 72.33 * np.power(S, -0.5)
    
    elif inversion == "interpolation":
        return angular2kappa(S)
    
    else:
        raise ValueError()