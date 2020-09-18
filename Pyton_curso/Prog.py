from sympy import *
from numpy import linspace
import numpy as np
import matplotlib.pyplot as pl
x = Symbol('x')

f = x**2-3
g = x**3

fx = lambdify(x,f, modules=['numpy'])
gx = lambdify(x,g, modules=['numpy'])

xvals = linspace(-10, 10, 100)
yvals = linspace(1, 2, 100)

pl.plot(xvals, fx(xvals), xvals, gx(xvals))
pl.plot(xvals, yvals)
pl.show()

print(type(xvals))


lista = []

lista.append(5)
num = np.array(lista)

print(num)
lista.append(6)
num = np.array(lista)
print(num)



