import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    k = np.arange(N).reshape(N, 1)
    n = np.arange(N).reshape(1, N)

    kn_matrix = k * n

    W = np.exp(-1j * 2 * np.pi * kn_matrix / N)
    
    return W

