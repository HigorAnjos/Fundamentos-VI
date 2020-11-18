from sympy import *

x = Symbol('x')
v = -1
if v <= 2:
    f = 3
else:
    f = 2*x-7

fx = lambdify(x, f, modules=['numpy'])

print(f(v))

