import sympy
from sympy import *
a, b, c = symbols('a, b, c')
matrix = sympy.Matrix([[1, 12, 43], [3, 4, 54], [3, 3, 54]])
print(matrix)
system = sympy.Matrix(((1, 4, 2), (-2, 1, 14)))
re = solve_linear_system(system, a, b)
print(re)
print(re[b])
is_li = true
for x in re:
    if re[x] != 0:
        is_li = False
        break
