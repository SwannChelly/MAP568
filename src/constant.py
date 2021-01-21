#### Constant file containing what we need for the project ####
import numpy as np 


# np.random.seed(1234)

# Date 
start_time  = '2020-01-25'
middle_time = '2020-02-24'
end_time    = '2020-03-15'

N_VARIABLE  = 10
deltaT      = 1
T_MAX       = 100
set_size    = int(T_MAX/deltaT)




cst = {}


cst_range = {
    'p_a'       : [0.4,0.9],
    'p_IH'      : [0.05,0.2],
    'p_IU'      : [0.01,0.04],
    'p_HD'      : [0.1,0.2],
    'p_HU'      : [0.1,0.2],
    'p_UD'      : [0.2,0.4],
    'R_0'       : [2.9,3.4],
    'mu'        : [0.01,0.08],
    'lambda_1'  : [10**(-4),10**(-3)]
}


def init_constant():

    cst['S_0'] = 67*10**6

    for key,value in cst_range.items() : 
        cst[key] = np.random.uniform(value[0],value[1])

    
    cst['t_0']      = init_random_date(start_time,middle_time)
    cst['N']        = init_random_date(middle_time,end_time)
    cst['N_I']      = np.random.randint(8,12)
    cst['N_H']      = np.random.randint(15,25)
    cst['N_U']      = np.random.randint(10,20)
    cst['I_moins_0']= np.random.randint(1,100)
    cst['lambda_2'] = 0

    cst['gamma_IR']    = (cst['p_a'] + (1-(cst['p_a'])*(1-cst['p_IH']-cst['p_IU'])))/cst['N_I']
    cst['gamma_IH']    = (1-(cst['p_a'])*cst['p_IH'])/cst['N_I']
    cst['gamma_IU']    = (1-(cst['p_a'])*cst['p_IU'])/cst['N_I']
    cst['gamma_HD']    = cst['p_HD']/cst['N_H']
    cst['gamma_HU']    = cst['p_HU']/cst['N_H']
    cst['gamma_HR']    = (1-cst['p_HD']-cst['p_HU'])/cst['N_H']
    cst['gamma_UD']    = cst['p_UD']/cst['N_U']
    cst['gamma_UR']    = (1-cst['p_UD'])/cst['N_U']
    cst['tau_0']       = cst['R_0']*(cst['lambda_1']+cst['gamma_IR'] + cst['gamma_IH'] + cst['gamma_IU'])/cst['S_0']
    cst['t']           = np.array([cst['t_0']+i*deltaT for i in range(set_size)])
    cst['tau']         = [cst['tau_0']*np.exp(-cst['mu']*np.max(cst['t'][i]-cst['N'],0)) for i in range(set_size)]
    

    return cst

def init_random_date(start_time,end_time,integer = True,first_date ='2020-01-25'):
    first_date = np.datetime64(first_date)
    start_time = np.datetime64(start_time)
    end_time   = np.datetime64(end_time)
    bimonthly_days = np.arange(0, (end_time-start_time))
    random_date = start_time + np.random.choice(bimonthly_days)
    if integer : 
        return (random_date-first_date).astype(int)
    return random_date + (start_time-first_date).astype(int)


# We define constants
init_constant() 


S_0         = cst['S_0']
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

gamma_IR    = cst['gamma_IR']
gamma_IH    = cst['gamma_IH']
gamma_IU    = cst['gamma_IU']
gamma_HD    = cst['gamma_HD']
gamma_HU    = cst['gamma_HU']
gamma_HR    = cst['gamma_HR']
gamma_UD    = cst['gamma_UD']
gamma_UR    = cst['gamma_UR']
tau_0       = cst['tau_0']


t           = cst['t']
tau         = cst['tau']





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
