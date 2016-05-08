import pprint
import numpy as np
import scipy

def lu(A):

	# Retorna error en caso de que la matriz no sea cuadrada
	if not A.shape[0] == A.shape[1]:
		raise ValueError("Input matrix must be square")
	
	#Orden de la matriz
	n = A.shape[0] 
	
	L = np.zeros((n,n),dtype='float64') 
	U = np.zeros((n,n),dtype='float64') 
	U[:] = A 
	np.fill_diagonal(L,1) #LLena la diagonal L con 1

	for i in range(n-1):
		for j in range(i+1,n):
			L[j,i] = U[j,i]/U[i,i]
			U[j,i:] = U[j,i:]-L[j,i]*U[i,i:]
			U[j,i] = 0
	return (L,U)
    
def luEquation(A, b):
	L, U = lu(A)
	
	#Primero se resuelve Ly = b
	y = np.linalg.solve(L, b)
	
	#Despues se resuleve Ux = y
	x = np.linalg.solve(U, y)
	
	return x

A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])
b = np.array([11, 70, 17])

x = luEquation(A, b)

pprint.pprint(x)


'''   
#A = np.array([[1,2,3], [4,5,6], [0,3,6]])
A = np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
print ("A: ")
pprint.pprint (A)
L, U = lu(A)
print ("L: ")
pprint.pprint (L)
print ("U: ")
pprint.pprint (U)
'''
