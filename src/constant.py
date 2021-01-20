#### Constant file containing what we need for the project ####
import numpy as np 


np.random.seed(1234)

# Date 
start_time  = '2020-01-25'
middle_time = '2020-02-04'
end_time    = '2020-03-15'

N_VARIABLE  = 10
S_0         = 67*10**6
deltaT      = 1
T_MAX       = 10
t           = np.array([i for i in range(T_MAX)])



cst = {}


cst_range = {
    'p_a'       : [0.4,0.9],
    'p_IH'      : [0.05,0.2],
    'p_IU'      : [0.01,0.04],
    'p_HD'      : [0.1,0.2],
    'p_HU'      : [0.1,0.2],
    'p_UD'      : [0.2,0.4],
    'N_I'       : [8,12],
    'N_H'       : [15,25],
    'N_U'       : [10,20],
    'R_0'       : [2.9,3.4],
    'mu'        : [0.01,0.08],
    'I_moins_0' : [1,100],
    'lambda_1'  : [10**(-4),10**(-3)]
}


def init_constant():

    for key,value in cst_range.items() : 
        cst[key] = np.random.uniform(value[0],value[1])

    cst['N']        = init_random_date(middle_time,end_time)
    cst['t_0']      = init_random_date(start_time,end_time)
    cst['lambda_2'] = 0

    return cst

def init_random_date(start_time,end_time,integer = True):
    start_time = np.datetime64(start_time)
    end_time = np.datetime64(end_time)
    bimonthly_days = np.arange(0, (end_time-start_time))
    random_date = start_time + np.random.choice(bimonthly_days)
    if integer : 
        return (random_date-start_time).astype(int)
    return random_date


# We define constants
init_constant() 

p_a         = cst['p_a']
p_IH        = cst['p_IH']
p_IU        = cst['p_IU']
p_HD        = cst['p_HD']
p_HU        = cst['p_HU']
p_UD        = cst['p_UD']
N_I         = cst['N_I']
N_H         = cst['N_H']
N_U         = cst['N_U']
R_0         = cst['R_0']
mu          = cst['mu']
I_moins_0   = cst['I_moins_0']
lambda_1    = cst['lambda_1']
lambda_2    = cst['lambda_2']
N           = cst['N']
t_0         = cst['t_0']

gamma_IR    = (p_a + (1-p_a)*(1-p_IH-p_IU))/N_I
gamma_IH    = (1-p_a)*p_IH/N_I
gamma_IU    = (1-p_a)*p_IU/N_I
gamma_HD    = p_HD/N_H
gamma_HU    = p_HU/N_H
gamma_HR    = (1-p_HD-p_HU)/N_H
gamma_UD    = p_UD/N_U
gamma_UR    = (1-p_UD)/N_U
tau_0       = R_0*(lambda_1+gamma_IR + gamma_IH + gamma_IU)/S_0

tau = tau_0*np.exp(-mu*np.max(t-N,0))


# matrix_coordinates  = {
#     'S':0,
#     'I_moins':1,
#     'I_plus':2,
#     R_moins:3,
#     R_plus_I:4,
#     H:5,
#     U:6,
#     R_plus_H:7,
#     D:8,
#     D_R:9
# }
