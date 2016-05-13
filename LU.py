import pprint
import numpy as np
import scipy
import warnings

warnings.filterwarnings('error')

def lu(A):
	n = A.shape[0] 	# Orden de la matriz
	L = np.zeros((n,n),dtype='float64') 
	U = np.zeros((n,n),dtype='float64') 
	U[:] = A 
	np.fill_diagonal(L,1) #LLena la diagonal L con 1
	
	#Si U[j,i]/U[i,i] es division de 0, no tiene factorizacion
	#se ejecuta el except
	
	try:
	
		for i in range(n-1):
			for j in range(i+1,n):
				L[j,i] = U[j,i]/U[i,i]
				U[j,i:] = U[j,i:]-L[j,i]*U[i,i:]
				U[j,i] = 0
			pprint.pprint(L)
			pprint.pprint(U)
				
		return (L,U)
	
	except Warning:
		
		return "No tiene inversa"
	
	


def luEquation(A, b):
	
	L, U = lu(A)
	
	#Primero se resuelve Ly = b
	y = np.linalg.solve(L, b)
		
	#Despues se resuleve Ux = y
	x = np.linalg.solve(U, y)
	
	return x


def luInverse(A):
	L, U = lu(A)
	# Primero se resuelve la inversa de L
	LInv = np.linalg.inv(L)
	
	#Despues se resuelve la invers de U
	UInv = np.linalg.inv(U)
	
	#Al final se multiplican ambas inversas para resolver A inverso
	AInv = np.dot(LInv, UInv)
	
	return AInv, LInv, UInv
	
	
A = np.array([[0, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
try:
	print ("A: ")
	pprint.pprint (A)
	L, U = lu(A)
	print ("L: ")
	pprint.pprint (L)
	print ("U: ")
	pprint.pprint (U)
	
except ValueError:
	print (lu(A))

#Valores de prueba
'''
A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])

AInv, LInv, UInv = luInverse(A)

pprint.pprint(AInv)
pprint.pprint(LInv)
pprint.pprint(UInv)


#A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])
A = np.array([[-15, -6, 9], [35, -4, -12], [-30, 36, -16]])
b = np.array([0, -9, -6])

x = luEquation(A, b)


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

#Funciones de prueba
'''
def upperSol(A, b):
    n = np.size(b)
    x = np.zeros_like(b)

    x[-1] = 1. / A[-1, -1] * b[-1]
    for i in range(n-2, -1, -1):
        x[i] = 1. / A[i, i] * (b[i] - np.sum(A[i, i+1:] * x[i+1:]))

    return x

	
def steps(A, b, x):
	for i in range (len (x)):
		print(str(A[i]) + " = " + str(b[i]) + ", " + "x" + str(i + 1) + ": " + str(x[i]))
		
def luEquation(A, b):
	
	L, U = lu(A)
	
	pprint.pprint (L)
	pprint.pprint (U)
	
	print("\n\n")
	
	#Primero se resuelve Ly = b
	y = np.linalg.solve(L, b)
	steps (L, b, y)
	
	print("\n\n")
	
	#Despues se resuleve Ux = y
	x = np.linalg.solve(U, y)
	steps (U, y, x)
	
	return x
	
A = np.array([[0, -3, 3], [5, -2, -2], [5, -2, -2], [5, -2, -2], [5, -2, -2]])

A = A.T

b = np.array([0, 0, 0])

pprint.pprint(A)

x = np.linalg.lstsq(A, b)

isLinear = True

if x[2] != len(A[0]):
	isLinear = False
else:
	isLinear = True

for i in range(len(x[0])):
 if x[0][i] != 0:
		isLinear = False


print ("Is LI: " + str(isLinear))
'''
