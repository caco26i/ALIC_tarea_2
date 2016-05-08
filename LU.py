import pprint
import numpy as np
import scipy

def lu(A):

    # Return an error if matrix is not square
    if not A.shape[0]==A.shape[1]:
        raise ValueError("Input matrix must be square")

    n = A.shape[0] 

    L = np.zeros((n,n),dtype='float64') 
    U = np.zeros((n,n),dtype='float64') 
    U[:] = A 
    np.fill_diagonal(L,1) # fill the diagonal of L with 1

    for i in range(n-1):
        for j in range(i+1,n):
            L[j,i] = U[j,i]/U[i,i]
            U[j,i:] = U[j,i:]-L[j,i]*U[i,i:]
            U[j,i] = 0
    return (L,U)
    
#A = np.array([[1,2,3], [4,5,6], [0,3,6]])
A = np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
print ("A: ")
pprint.pprint (A)
L, U = lu(A)
print ("L: ")
pprint.pprint (L)
print ("U: ")
pprint.pprint (U)
