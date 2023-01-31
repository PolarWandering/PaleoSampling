import numpy as np
import pandas as pd
import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag

N_sample = 20000

all_kappa = 10 ** np.linspace(0, 4, 200)
all_stds = []

for kappa in all_kappa:

    dec, inc = ipmag.fishrot(k=kappa,
                              n=N_sample, 
                              dec=0, 
                              inc=90, 
                              di_block=False)
    
    angular_std = np.linalg.norm(90 - np.array(inc)) / np.sqrt(len(inc))
    all_stds.append(angular_std)
    
    
df = pd.DataFrame({'kappa': all_kappa, 'std_angular': all_stds})
df.to_csv("kappa2angular.csv")