import numpy as np
from numpy.testing import assert_allclose
import smpsite as smp

def test_run_kappa_from_latitude():
    _res = smp.kappa_from_latitude(10.0, degrees=True)
    assert isinstance(_res, np.ndarray)
    assert _res.shape == ()
    
def test_run_lat_correction():
    _res = smp.lat_correction(30.0, degrees=True)
    assert_allclose(_res, 1.2578124999999998, atol=1e-6)