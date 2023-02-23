"""
Set of tools for the sampling of paleomagnetic data

This includes:
    - 
"""

__version__ = "0.0.1"
__all__ = ["estimate", "sampling", "kappa"]

from .kappa import *
from .sampling import *
from .estimate import *
