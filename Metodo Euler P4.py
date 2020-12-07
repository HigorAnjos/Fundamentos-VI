from sympy import *

x = Symbol('x')
y = Symbol('y')

v = 5
k = 0.12
c = 12
f = (c/x)/v - k*y

h = 1
xn = 0
yn = 12.5


while xn < 13:
    xn = xn + h
    yn = yn + h * f.subs(x, xn).subs(y, yn)

print(f'{xn}Min a concentracao de glicose é = {yn} mg')


