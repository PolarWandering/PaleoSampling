import numpy as np
import pandas as pd
import pathlib
from scipy import interpolate

_file_location = pathlib.Path(__file__).parent.joinpath("kappa_tabular/kappa2angular.csv")#.parent.joinpath("")
df = pd.read_csv(_file_location, header=0)

kappa2angular = interpolate.interp1d(df.kappa, df.std_angular)
angular2kappa = interpolate.interp1d(df.std_angular, df.kappa)


def kappa_from_latitude(latitude, a = 11.23, b=0.27, degrees = False, inversion="interpolation"):
    """
    Calculate the theoretical concentration parameter (kappa) for a sample of VGPs at a given latitude using Model G.
    
    Args:
        latitude (float): Latitude value in radians unless specified otherwise.
        a (float, optional): Parameter 'a' of Model G. Defaults to 11.23.
        b (float, optional): Parameter 'b' of Model G. Defaults to 0.27.
        degrees (bool, optional): If True, the input latitude is in degrees. Defaults to False.
        inversion (str, optional): Method used to determine kappa from angular dispersion. 
                                   Can be "power-law" or "interpolation". Defaults to "interpolation".
                                   
    Returns:
        float: Theoretical concentration parameter (kappa) for a sample of VGPs at the given latitude.
    
    Notes:
        - Employs a power-law fit for the relation between kappa and angular dispersion: \( S = 72.33 \kappa^{-0.50} \).
        - Default 'a' and 'b' values are sourced from Doubrovine et al., 2019, representing the last 10 Ma (PSV10).
    
    References:
        - Doubrovine, P. V., Veikkolainen, T., Pesonen, L. J., Piispa, E., Ots, S., Smirnov, A. V., et al. (2019). 
          Latitude dependence of geomagnetic paleosecular variation and its relation to the frequency of magnetic 
          reversals: Observations from the Cretaceous and Jurassic. Geochemistry, Geophysics, Geosystems, 20, 1240–1279. 
          https://doi.org/10.1029/2018GC007863
          
        - McFadden, P. L., Merrill, R. T., & McElhinny, M. W. (1988). Dipole/quadrupole family modeling of paleosecular 
          variation. Journal of Geophysical Research, 93(B10), 11,583–11,588. 
          https://doi.org/10.1029/JB093iB10p11583
    
    Raises:
        ValueError: If an unsupported inversion method is provided.
    """
    
    if degrees == False: 
        latitude = np.degrees(np.abs(latitude))
        
    # Model G from Doubrovine et al. 2019  
    S = np.sqrt( a ** 2 + ( latitude * b ) ** 2 ) 
    
    if inversion == "power-law":
        return 72.33 * np.power(S, -0.5)
    
    elif inversion == "interpolation":
        return angular2kappa(S)
    
    else:
        raise ValueError()
        
def lat_correction(lat, degrees=True):
    """
    Calculates the latitude correction based on formula from Cox (1970).

    Args:
        lat (float): Latitude value.
        degrees (bool, optional): Indicates if the given latitude is in degrees. Defaults to True.

    Returns:
        float: Angular variance of VGPs as function of latitude.

    References:
        Cox, A. (1970). Latitude Dependence of the Angular Dispersion of the Geomagnetic Field. 
        Geophysical Journal International, 20(3), 253–269. https://doi.org/10.1111/j.1365-246X.1970.tb06069.x
    """
    if degrees:
        _lat = lat * np.pi / 180
    sn2 = np.sin(_lat) ** 2
    return (5 + 18 * sn2 + 9 * sn2**2) / 8