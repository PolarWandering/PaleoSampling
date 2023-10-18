import numpy as np
from numpy.testing import assert_allclose
import smpsite as smp

def test_run_kappa_from_latitude():
    _res = smp.kappa_from_latitude(10.0, degrees=True)
    assert isinstance(_res, np.ndarray)
    assert _res.shape == ()

def test_kappa_from_latitude():
    _degs = [10, 50, 80]
    _res  = [49.5176626866052, 21.698350477271674, 11.416853315971776]
    for i, _deg in enumerate(_degs):
        kappa1 = float(smp.kappa_from_latitude(_deg, degrees = True))
        kappa2 = float(smp.kappa_from_latitude(_deg/180.0*np.pi, degrees = False))
        assert_allclose(kappa1, kappa2, rtol=1e-6)
        assert_allclose(kappa1, _res[i], rtol=1e-6)

def test_kappa_from_latitude_power():
    kappa = float(smp.kappa_from_latitude(10.00, degrees = True, inversion="power-law"))
    assert_allclose(kappa, 21.282720785612874, rtol=1e-6)
        
def test_run_lat_correction():
    _res = smp.lat_correction(30.0, degrees=True)
    assert_allclose(_res, 1.2578124999999998, atol=1e-6)

