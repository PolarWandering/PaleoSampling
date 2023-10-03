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

def test_params_read():
    assert params0.N == 10 and params0.site_lat == 10

def test_desing():
    assert np.array_equal(smp.generate_design(params0), [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

def test_sample():
    _df = smp.generate_samples(params0)
    assert isinstance(_df, pd.DataFrame)
    assert _df.shape == (50,6)
    for col in ['sample_site', 'vgp_long', 'vgp_lat', 'vgp_dec', 'vgp_inc', 'is_outlier']:
        assert col in _df.columns
    
