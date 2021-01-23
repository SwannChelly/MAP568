from __future__ import division
import numpy as np 
from constant import *
from utils import * 
import random
import matplotlib.pyplot as plt
from scipy import *
from pylab import *     
from scipy.integrate import odeint # Module de résolution des équations différentielles


from constant import *




# First define the matrix : 

# np.random.seed(1234)


#Res = Resolution_Systeme(set_size, deltaT,S_0)
#print(Res[1])  ##### nombre d'infectés

start = 0
end = T_MAX
numsteps = set_size
time = np.linspace(start,end,numsteps)
#i = 0
#for i in range(len(time)):
#    time[i]=round(time[i],1)
#time = list(time)   
   



def equa_diff(syst,temps):
    #temps = round(temps,1)
    #if temps == 50:
    #    temps = 50.1
    #elif temps > 100.:
    #    temps = 100.
    #i = time.index(temps)
    tau = cst['tau_0']*np.exp(-cst['mu']*np.max(temps-(cst['N']-cst['t_0']),0))
    S = syst[0] 
    I_moins = syst[1] 
    I_plus = syst[2] 
    R_moins = syst[3] 
    R_plus_I = syst[4] 
    H = syst[5] 
    U = syst[6] 
    R_plus_H = syst[7] 
    D = syst[8] 
    D_R = syst[9]
    # Dérivées des variables
    DS = -tau*S*I_moins
    DI_moins = tau*S*I_moins-cst['lambda_1']*I_moins-(cst['gamma_IR']+cst['gamma_IH']+cst['gamma_IU'])*I_moins
    DI_plus = cst['lambda_1']*I_moins-(cst['gamma_IR']+cst['gamma_IH']+cst['gamma_IU'])*I_plus
    DR_moins = cst['gamma_IR']*I_moins-cst['lambda_2']*R_moins
    DR_plus_I = cst['gamma_IR']*I_plus+cst['lambda_2']*R_moins
    DH = cst['gamma_IH']*(I_moins + I_plus)-(cst['gamma_HR']+cst['gamma_HD']+cst['gamma_HU'])*H
    DU = cst['gamma_IU']*(I_moins + I_plus)+cst['gamma_HU']*H-(cst['gamma_UR'] + cst['gamma_UD'])*U
    DR_plus_H = cst['gamma_HR']*H+cst['gamma_UR']*U
    DD = cst['gamma_UD']*U+cst['gamma_HD']*H  
    DD_R = (cst['lambda_1']+cst['gamma_IH']+cst['gamma_IU'])*I_moins-D_R
    
    
    return(DS,DI_moins,DI_plus,DR_moins,DR_plus_I,DH,DU,DR_plus_H,DD,DD_R)



def pic_epidemie(L):
    #### L une liste 
    maximum = np.max(L)
    N_jours_pic = L.index(maximum)
    return (maximum, N_jours_pic)

def Monte_Carlo(M):
    MAX = []
    N_MAX = []
    for i in range(M):
        print(i)
        cst = init_constant()
        syst_CI=array([cst['S_0'],cst['I_moins_0'],0,0,0,0,0,0,0,0]) 
        Sols=odeint(equa_diff,syst_CI,t)   
        #print(Resultat[6])
        max_patients, N_jours_max = pic_epidemie(list(Sols[:,6]))
        #print(cst)
        MAX +=[max_patients]
        N_MAX +=[N_jours_max]
    return (MAX,N_MAX)
    

cst = init_constant()
syst_CI=array([cst['S_0'],cst['I_moins_0'],0,0,0,0,0,0,0,0])
Sols=odeint(equa_diff,syst_CI,t)
plt.plot(Sols[:,1])
 
#MAX, N_MAX = Monte_Carlo(100)
#plt.hist(MAX, bins = 30)    
    
