# Constant file containing what we need for the project ####
import numpy as np 
from scipy.stats import lognorm
from scipy.stats import norm 
from scipy.stats import halfcauchy



# np.random.seed(1234)

# Date 
start_time  = '2020-01-25'
middle_time = '2020-02-24'
end_time    = '2020-03-15'



global_constants = {'deltaT':1,
'T_MAX': 100, 
'S_0': 67*10**6}

global_constants['set_size'] = int(global_constants['T_MAX']/global_constants['deltaT'])


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

bound = ((0.4,0.9),(0.05,0.2),(0.01,0.04),(0.1,0.2),(0.1,0.2),(0.2,0.4),(2.9,3.4),(0.01,0.08),(10**(-4),10**(-3)),(0,30),(30,50),
(8,12),(15,25),(10,20),(1,100))



def init_random_date(start_time,end_time,integer = True,first_date ='2020-01-25'):
    first_date = np.datetime64(first_date)
    start_time = np.datetime64(start_time)
    end_time   = np.datetime64(end_time)
    bimonthly_days = np.arange(0, (end_time-start_time))
    random_date = start_time + np.random.choice(bimonthly_days)
    if integer : 
        return (random_date-first_date).astype(int)
    return random_date + (start_time-first_date).astype(int)


def init_variables(deltaT= 1,T_MAX= 100, global_constants = global_constants):
    variables = {}
    global_constants['deltaT'] = deltaT
    global_constants['T_MAX']   = T_MAX
    global_constants['set_size']= int(T_MAX/deltaT)  

    for key,value in cst_range.items() : 
        variables[key] = np.random.uniform(value[0],value[1])
        
    variables['t_0']      = np.random.randint(1,31)
    variables['N']        = np.random.randint(30,51)
    variables['N_I']      = np.random.randint(8,13)
    variables['N_H']      = np.random.randint(15,26)
    variables['N_U']      = np.random.randint(10,21)
    variables['I_moins_0']= np.random.randint(1,101)

    return variables

variables = init_variables(global_constants=global_constants)


def compute_constants(variables,global_constants= global_constants):
    """
    This function takes the constants created by the random choice of the constants.
    """
    constants = {}
    constants['gamma_IR']    = (variables['p_a'] + (1-variables['p_a'])*(1-variables['p_IH']-variables['p_IU']))/variables['N_I']
    constants['gamma_IH']    = (1-variables['p_a'])*variables['p_IH']/variables['N_I']
    constants['gamma_IU']    = (1-variables['p_a'])*variables['p_IU']/variables['N_I']
    constants['gamma_HD']    = variables['p_HD']/variables['N_H']
    constants['gamma_HU']    = variables['p_HU']/variables['N_H']
    constants['gamma_HR']    = (1-variables['p_HD']-variables['p_HU'])/variables['N_H']
    constants['gamma_UD']    = variables['p_UD']/variables['N_U']
    constants['gamma_UR']    = (1-variables['p_UD'])/variables['N_U']
    constants['tau_0']       = variables['R_0']*(variables['lambda_1']+constants['gamma_IR'] + constants['gamma_IH'] + constants['gamma_IU'])/global_constants['S_0']
    constants['t']           = np.arange(int(variables['t_0']),int(variables['t_0'])+global_constants['set_size'],global_constants['deltaT'])
    constants['tau']         = constants['tau_0']*np.exp(-variables['mu']*np.maximum(constants['t']-variables['N'],0))

    return constants

constants = compute_constants(variables= variables, global_constants=global_constants)

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def merge_parameters(constants = constants,variables = variables, global_constants = global_constants):
    all_parameters = merge_two_dicts(variables,constants) 
    all_parameters = merge_two_dicts(all_parameters,global_constants)
    return all_parameters

def init_all_parameters(global_constants=global_constants):
    variables = init_variables(global_constants=global_constants)
    constants = compute_constants(variables= variables,global_constants= global_constants)
    return merge_parameters(constants = constants,variables = variables, global_constants = global_constants)




variables_keys = list(variables.keys())
constants_keys = list(constants.keys())


# We define constants

all_parameters = init_all_parameters(global_constants=global_constants)


# Constant 

n_DR = 30
n_H  = 52

# Pandas short-cut

jour = 'jour'


# Function keys 

F = {'p_a': 'lognorm',
    'p_IH': 'lognorm',
    'p_IU': 'lognorm',
    'p_HD': 'lognorm',
    'p_HU': 'lognorm',
    'p_UD': 'lognorm',
    'N_I' : 'lognorm',
    'N_H' : 'lognorm',
    'N_U' : 'lognorm',
    'R_0' : 'lognorm',
    'mu'  : 'lognorm',
    'N'   : 'norm',
    't_0'   : 'norm',
    'I_moins_0' : 'lognorm',
    'lambda_1' : 'lognorm'
}

F_parameters = {'p_a': {'scale':0.65,'s':0.1},
    'p_IH': {'scale':0.125,'s':0.1},
    'p_IU': {'scale':0.025,'s':0.1},
    'p_HD': {'scale':0.15,'s':0.1},
    'p_HU': {'scale':0.15,'s':0.1},
    'p_UD': {'scale':0.3,'s':0.1},
    'N_I' : {'scale':10,'s':0.1},
    'N_H' : {'scale':20,'s':0.1},
    'N_U' : {'scale':15,'s':0.1},
    'R_0' : {'scale':3.15,'s':0.1},
    'mu'  : {'scale':0.045,'s':0.1},
    'N'   : {'loc':40,'scale':1},
    't_0' : {'loc':15, 'scale':1},
    'I_moins_0' : {'scale':50,'s':0.1},
    'lambda_1' : {'scale':0.5*10**(-5),'s':0.1}
}


bounds = {'p_a': {'low':0.4,'high':0.9},
    'p_IH': {'low':0.05,'high':0.2},
    'p_IU': {'low':0.01,'high':0.04},
    'p_HD': {'low':0.1,'high':0.2},
    'p_HU': {'low':0.1,'high':0.2},
    'p_UD': {'low':0.2,'high':0.4},
    'N_I' : {'low':8,'high':12},
    'N_H' : {'low':15,'high':25},
    'N_U' : {'low':10,'high':20},
    'R_0' : {'low':2.9,'high':3.4},
    'mu'  : {'low':0.01,'high':0.08},
    'N'   : {'low':30,'high':50},
    't_0' : {'low':1, 'high':30},
    'I_moins_0' : {'low':1,'high':10},
    'lambda_1' : {'low':10**(-4),'high':10**(-3)}
}


