

class kappa2angular:
    
    def __init__(self, table):
        self.table = table
        
    def __call__(self, x):
        return self.table[x]
    
kappa_table = ...
kappa2angular = kappa2angular(kappa_table)