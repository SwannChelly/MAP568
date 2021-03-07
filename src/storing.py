F_current_parameters = {'p_a': {'scale':0.5,'loc':0.4,'constraint':'two','low':0,'high':1},
    'p_IH': {'scale':0.15,'loc':0.05,'constraint':'two','low':0,'high':1},
    'p_IU': {'scale':0.03,'loc':0.01,'constraint':'two','low':0,'high':1},
    'p_HD': {'scale':0.1,'loc':0.1,'constraint':'two','low':0,'high':1},
    'p_HU': {'scale':0.1,'loc':0.1,'constraint':'two','low':0,'high':1},
    'p_UD': {'scale':0.3,'loc':0.2,'constraint':'two','low':0,'high':1},
    'N_I' : {'scale':0.2,'loc':0.8,'constraint':'one','low':0},
    'N_H' : {'scale':4,'loc':0.15,'constraint':'one','low':0},
    'N_U' : {'scale':10,'loc':0.10,'constraint':'one','low':0},
    'R_0' : {'scale':0.5,'loc':2.9,'constraint':'None'},
    'mu'  : {'scale':0.07,'loc':0.01,'constraint':'None'},
    'N'   : {'scale':20,'loc':30,'constraint':'two', 'low':30,'high':50},
    't_0' : {'scale':30,'loc':0,'constraint':'two','low':0,'high':30},
    'I_moins_0' : {'scale':99,'loc':1,'constraint':'one','low':1},
    'lambda_1' : {'scale':9*10**(-4),'loc':10**(-4),'constraint':'None'}
}



F_parameters = {'p_a': {'scale':0.5,'loc':0.4,'constraint':'two','low':0,'high':1},
    'p_IH': {'scale':0.15,'loc':0.05,'constraint':'two','low':0,'high':1},
    'p_IU': {'scale':0.03,'loc':0.01,'constraint':'two','low':0,'high':1},
    'p_HD': {'scale':0.1,'loc':0.1,'constraint':'two','low':0,'high':1},
    'p_HU': {'scale':0.1,'loc':0.1,'constraint':'two','low':0,'high':1},
    'p_UD': {'scale':0.3,'loc':0.2,'constraint':'two','low':0,'high':1},
    'N_I' : {'scale':0.2,'loc':0.8,'constraint':'one','low':0},
    'N_H' : {'scale':4,'loc':0.15,'constraint':'one','low':0},
    'N_U' : {'scale':10,'loc':0.10,'constraint':'one','low':0},
    'R_0' : {'scale':0.5,'loc':2.9,'constraint':'None'},
    'mu'  : {'scale':0.07,'loc':0.01,'constraint':'None'},
    'N'   : {'scale':20,'loc':30,'constraint':'two', 'low':30,'high':50},
    't_0' : {'scale':30,'loc':0,'constraint':'two','low':0,'high':30},
    'I_moins_0' : {'scale':99,'loc':1,'constraint':'one','low':1},
    'lambda_1' : {'scale':9*10**(-4),'loc':10**(-4),'constraint':'None'}
}

F_parameters = {'p_a': {'loc':0.65,'scale':0.1},
    'p_IH': {'loc':0.125,'scale':0.1},
    'p_IU': {'loc':0.025,'scale':0.1},
    'p_HD': {'loc':0.15,'scale':0.1},
    'p_HU': {'loc':0.15,'scale':0.1},
    'p_UD': {'loc':0.3,'scale':0.1},
    'N_I' : {'loc':10,'scale':1},
    'N_H' : {'loc':20,'scale':1},
    'N_U' : {'loc':15,'scale':1},
    'R_0' : {'loc':3.15,'scale':0.1},
    'mu'  : {'loc':0.05,'scale':0.01},
    'N'   : {'loc':40,'scale':1},
    't_0' : {'loc':15, 'scale':1},
    'I_moins_0' : {'scale':50,'s':0.1},
    'lambda_1' : {'scale':0.5*10**(-5),'s':0.1}
}


F = {'p_a': 'beta',
    'p_IH': 'beta',
    'p_IU': 'beta',
    'p_HD': 'beta',
    'p_HU': 'beta',
    'p_UD': 'beta',
    'N_I' : 'norm',
    'N_H' : 'norm',
    'N_U' : 'norm',
    'R_0' : 'norm',
    'mu'  : 'norm',
    'N'   : 'norm',
    't_0'   : 'norm',
    'I_moins_0' : 'lognorm',
    'lambda_1' : 'norm'
}



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



F = {'p_a': 'beta',
    'p_IH': 'beta',
    'p_IU': 'beta',
    'p_HD': 'beta',
    'p_HU': 'beta',
    'p_UD': 'beta',
    'N_I' : 'norm',
    'N_H' : 'norm',
    'N_U' : 'norm',
    'R_0' : 'norm',
    'mu'  : 'norm',
    'N'   : 'norm',
    't_0'   : 'norm',
    'I_moins_0' : 'lognorm',
    'lambda_1' : 'lognorm'
}