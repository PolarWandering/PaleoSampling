import smpsite as smp
import numpy as np
import pandas as pd
from numpy.testing import assert_allclose

params0 = smp.Params(N=10,
                     n0=5,
                     kappa_within_site=100,
                     site_lat=10, 
                     site_long=0,
                     outlier_rate=0.10,
                     secular_method="G",
                     kappa_secular=None)

def test_robust_fisher_mean_single():
    _res = smp.robust_fisher_mean([10.0], [20.0])
    assert _res['vgp_dec'] == 10.0
    assert _res['vgp_inc'] == 20.0
    assert _res['n_samples'] == 1
    assert _res['resultant_length'] == 1.0

def test_robust_fisher_mean_multiple():
    _res = smp.robust_fisher_mean([10.0, 20.0], [0.0, 0.0])
    assert_allclose(_res['vgp_dec'], 15.0, 1e-6)

def test_estimate():

    # Read sample data created with these params
    df = pd.read_csv('./smpsite/test/data/df1.csv')

    _res = smp.estimate_pole(df, params0, ignore_outliers="True")

    assert_allclose(_res['pole_dec'], 350.20065867362314)
    assert_allclose(_res['pole_inc'], 86.75081527833235)
    assert_allclose(_res['S2_vgp'], 182.60923786776738)

    _res = smp.estimate_pole(df, params0, ignore_outliers="False")

    assert_allclose(_res['pole_dec'], 18.215514011721595)
    assert_allclose(_res['pole_inc'], 86.81743210088786)
    assert_allclose(_res['S2_vgp'], 99.71484820447859)

    _res = smp.estimate_pole(df, params0, ignore_outliers="vandamme")

    assert_allclose(_res['pole_dec'], 18.215514011721595)
    assert_allclose(_res['pole_inc'], 86.81743210088786)
    assert_allclose(_res['S2_vgp'], 99.71484820447859)

    
def test_simulate():
    _df = smp.simulate_estimations(params0, n_iters=10, ignore_outliers="True", seed=666)
    assert _df.shape == (10,17)
    for col in ['plong', 'plat', 'S2_vgp', 'error_angle']:
        assert col in _df.columns