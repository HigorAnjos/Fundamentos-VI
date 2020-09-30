import numpy as np
from sympy import *
from math import *
import matplotlib.pyplot as pl
import sympy as sp

from sympy.plotting import *
import matplotlib.pyplot as plt


# usado no for
eps = 1.0
while eps + 1 > 1:
    eps /= 2

eps *= 2

#  sinbolo x
x = Symbol('x')

#  Dinifina a funcao
f = x**4-12*x**3+47*x**2-60*x
fx = lambdify(x, f, modules=['numpy'])

#  Deriavada da funcao
d = diff(fx(x), x)
df = lambdify(x, d,  modules=['numpy']) # df(x)


#  Calular valores de x e por em indice_x
#  Gardar os resultados em indice_y


n = 1 #  Numero a se passar pra interacao 3 5 3 5

vetx = []
vety = []

interacao = 0

while (np.absolute(fx(n)) >= 0.00001):

    if df(n) != 0:                #  Adicionado o if
        vetx.append(n)
        n = n - (fx(n) / df(n))
        vety.append(n)
        interacao = interacao + 1       #  Adicionado a interacao




print(f"Interacoes {interacao}")

print(vety)

xval = np.array(vetx)
yval = np.array(vety)
grafico_val = np.linspace(-6, 6, 60)
#  Montar o grafico funcao

pl.plot(xval, fx(xval))

#pl.plot(1.73205080756888, fx(1.73205080756888), 'ro')




pl.plot(grafico_val, fx(grafico_val))

if interacao == 0:
    print(f"Raiz: {n}")

print("Raiz da funcao {}".format(solve(fx(x))))
print("Raiz da funcao {}".format(solve(N(fx(x)))))
pl.tight_layout()
#pl.show()
