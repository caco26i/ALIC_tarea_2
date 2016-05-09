import sympy
from sympy import *
a, b, c = symbols('a, b, c')
matrix = sympy.Matrix([[-1, 3], [2, 4]])
print(matrix)
re = solve_linear_system(matrix, a, b)
print(re)

is_li = true
for x in re:
    if re[x] != 0:
        is_li = False
        break
