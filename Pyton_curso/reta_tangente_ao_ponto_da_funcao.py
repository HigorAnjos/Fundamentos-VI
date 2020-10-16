import numpy as np
from sympy import *
from math import *
import matplotlib.pyplot as pl
x1 = -1

x = Symbol('x')

f = x**2/(x**2+1)
fx = lambdify(x, f, modules=['numpy'])

d = diff(fx(x), x)
df = lambdify(x, d,  modules=['numpy'])

print(f'Funcao {fx(x)}')
print(f'Derivada {df(x)} (coeficiente agular m)')

y1 = fx(x1)
#  (x1, y1)
#  Y - Y1 = m (X - X1)

funcao = df(x1)*x - df(x1)*x1 + y1

reta_tangente = lambdify(x, funcao, modules=['numpy'])


grafico_val = np.linspace(-4,4,2000)
grafico_reta = np.linspace(-4,4,100)
pl.plot(grafico_val, fx(grafico_val)) #  grafico da funcao
pl.plot(x1, fx(x1), 'ro')  #  Ponto x1 da funcao
pl.plot(grafico_val, reta_tangente(grafico_val))
pl.show()
