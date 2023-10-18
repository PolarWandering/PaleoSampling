"""
Set of tools for the sampling of paleomagnetic data

This includes the following modules:
    - .kappa       : Calculation of parameters of the Fisher distribution
    - .sampling    : Random sampling of paleopoles and samples in the sphere simulating a paleomagnetic study
    - .estimate    : Estimation of paleopole using Fisher means and secular variation
    - .theoretical : Theoretical calculations based on (Sapienza et al 2023)
"""

__version__ = "1.0.0"
__all__ = ["estimate", "sampling", "kappa", "theoretical"]

from .kappa import *
from .sampling import *
from .estimate import *
from .theoretical import *
