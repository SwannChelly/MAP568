import numpy as np 
from constant import *
from utils import * 
import random
import matplotlib.pyplot as plt

# First define the matrix : 

# np.random.seed(1234)


Res = Resolution_Systeme(set_size, deltaT,S_0)
#print(Res[1])  ##### nombre d'infectés


def pic_epidemie(L):
    #### L une liste 
    maximum = np.max(L)
    N_jours_pic = L.index(maximum)
    return (maximum, N_jours_pic)

def Monte_Carlo(M):
    MAX = []
    N_MAX = []
    for i in range(M):
        init_constant()
        Resultat = Resolution_Systeme(T_MAX, deltaT,S_0)
        #print(Resultat[6])
        max_patients, N_jours_max = pic_epidemie(list(Resultat[6]))
        #print(cst)
        MAX +=[max_patients]
        N_MAX +=[N_jours_max]
    return (MAX,N_MAX)
    
MAX, N_MAX = Monte_Carlo(10)
plt.plot(MAX, color = 'r')
plt.plot(N_MAX)
plt.show()


    
    
    