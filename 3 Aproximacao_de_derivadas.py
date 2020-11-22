from sympy import *
from numpy import *
from FuncoesCauchyNewton import *


hk = 1.
alf = 1/10

x_fun =  0.0001

x = Symbol('x')
fun = x**x
f = lambdify(x, fun, modules=['numpy'])

t = f(x_fun)

hk = alf*hk
yk = f(x_fun+hk)
deltak = hk**2 + (yk-t)**2

while deltak >= Epsilon():
    hk = alf * hk
    yk = f((x_fun + hk))
    deltak = hk ** 2 + (yk - t) ** 2

D = (yk-t)/hk

print(f'Resp = {round(D, 4)}')
print(D)

# resp Python -8.2 0278185039876
# resp geogeb -8.2027818503988