import pandas as pd
from scipy import interpolate

df = pd.read_csv("smpsite/smpsite/kappa_tabular/kappa2angular.csv", header=0)

kappa2angular = interpolate.interp1d(df.kappa, df.std_angular)
angular2kappa = interpolate.interp1d(df.std_angular, df.kappa)