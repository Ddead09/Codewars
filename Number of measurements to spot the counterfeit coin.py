from math import *
def how_many_measurements(n):
    if n==1:
        return 0
    
    else:
        return ceil(log(n,3))
