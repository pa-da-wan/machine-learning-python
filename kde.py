from os import EX_SOFTWARE
import numpy as np

# samples = np.random.normal(0, 1, 100)
def kde(samples, h):
    # compute density estimation from samples with KDE
    # Input
    #  samples    : DxN matrix of data points
    #  h          : (half) window size/radius of kernel
    # Output
    #  estDensity : estimated density in the range of [-5,5]

    #####Insert your code here for subtask 5a#####
    # Compute the number of samples created
    N = len(samples)
    pos = np.arange(-5, 5, 0.1).reshape(-1,1)
    gaussKernel = np.exp(-(pos-samples.reshape(-1,N))**2/(2*h**2))/(np.sqrt(2*np.pi)*h)
    prob = np.sum(gaussKernel,axis = 1,keepdims=True)/N
    estDensity = np.hstack((pos, prob)) #why does np.stack not work here? it outputs 100x2x1 matrix
    
    return estDensity
# kde(samples,0.3) 