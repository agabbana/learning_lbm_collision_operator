import numpy as np
from tensorflow.keras import backend as K
from numba import jit

def rmsre(y_true, y_pred, eps=1e-8):
    return K.sqrt( K.mean( K.square( (y_true - y_pred) / (y_true + eps) ), axis=-1) )

def LB_stencil():
    
    ###########################################################
    # D2Q9 stencil 
    Q = 9
    c = np.zeros((Q, 2), dtype=np.int32)
    w = np.zeros(Q)    
            
    cs2     = 1./3.
    qorder  = 2

    c[0, 0] =  0;  c[0, 1] =  0; w[0] = 4./9.
    c[1, 0] =  1;  c[1, 1] =  0; w[1] = 1./9.
    c[2, 0] =  0;  c[2, 1] =  1; w[2] = 1./9.
    c[3, 0] = -1;  c[3, 1] =  0; w[3] = 1./9.
    c[4, 0] =  0;  c[4, 1] = -1; w[4] = 1./9.
    c[5, 0] =  1;  c[5, 1] =  1; w[5] = 1./36.
    c[6, 0] = -1;  c[6, 1] =  1; w[6] = 1./36.
    c[7, 0] = -1;  c[7, 1] = -1; w[7] = 1./36.
    c[8, 0] =  1;  c[8, 1] = -1; w[8] = 1./36.

    ###########################################################
    # Function for the calculation of the equilibrium
    @jit
    def compute_feq(feq, rho, ux, uy, c, w):

        uu = (ux**2 + uy**2)*(1./cs2)

        for ip in range(Q):

            cu = (c[ip, 0]*ux[:,:]  + c[ip, 1]*uy[:,:] )*(1./cs2)

            feq[:, :, ip] = w[ip]*rho*(1.0 + cu + 0.5*(cu*cu - uu) )

        return feq
    
    ###########################################################

    return c, w, cs2, compute_feq

