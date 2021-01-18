import numpy as np 
from constant import *
from utils import * 

# First define the matrix : 

Res = np.zeros((N_VARIABLE,T_MAX))
Res[0,0] = S_0