import smpsite as smp
from numpy.testing import assert_allclose

params0 = smp.Params(N=10,
                     n0=5,
                     kappa_within_site=100,
                     site_lat=10, 
                     site_long=0,
                     outlier_rate=0.10,
                     secular_method="G",
                     kappa_secular=None)

def test_kappa_theoretical():
    assert_allclose(smp.kappa_theoretical(params0), 259.0223874154575)