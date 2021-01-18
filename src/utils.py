import numpy as np
from datetime import date
from constant import *



def euler_one_step(S,I_moins,I_plus,R_moins,R_plus_I,H,U,R_plus_H,D,D_R):
    
    S_1 = S-tau*S*I_moins*deltaT
    I_moins_1 = I_moins + (tau*S*I_moins-lambda_1*I_moins-(gamma_IR+gamma_IH+gamma_IU)*I_moins)*deltaT
    I_plus_1 = I_plus +(lambda_1*I_moins-(gamma_IR+gamma_IH+gamma_IU)*I_plus)*deltaT
    R_moins_1 = R_moins +(gamma_IR*I_moins-lambda_2*R_moins)*deltaT
    R_plus_I_1 = R_plus_I + (gamma_IR*I_plus+lambda_2*R_moins)*deltaT
    H_1 = H + (gamma_IH*(I_moins + I_plus)-(gamma_HR+gamma_HD+gamma_HU)*H)*deltaT
    U_1 = U + (gamma_IU*(I_moins + I_plus)+gamma_HU*H-(gamma_UR + gamma_UD)*U)*deltaT
    R_plus_H_1 = R_plus_H+ (gamma_HR*H+gamma_UR*U)*deltaT
    D_1 = D + (gamma_UD*U+gamma_HD*H)*deltaT  
    D_R_1 = D_R +((lambda_1+gamma_IH+gamma_IU)*I_moins-D_R)*deltaT
    
    
    return(S_1,I_moins_1,I_plus_1,R_moins_1,R_plus_I_1,H_1,U_1,R_plus_H_1,D_1,D_R_1)





