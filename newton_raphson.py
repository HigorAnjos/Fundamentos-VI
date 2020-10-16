import numpy as np
from sympy import *
from math import *
import matplotlib.pyplot as pl
import sympy as sp

from sympy.plotting import *
import matplotlib.pyplot as plt



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



# n = 0.5 # Raiz raphson 0
# n = 1 # Raiz raphson 5
# n = 2 # Raiz raphson 3
# n = 3.4556 # Raiz raphson 5
n = 3.6 #ache o 4




vetx = []
vety = []

interacao = 0
print()
while ( np.linalg.norm(fx(n)) >= 0.00001):

    if df(n) != 0:                #  Adicionado o if
        vetx.append(n)
        n = n - (fx(n) / df(n))
        vety.append(n)
        interacao = interacao + 1       #  Adicionado a interacao




print(f"Interacoes {interacao}")

#print(vety)

xval = np.array(vetx)
yval = np.array(vety)
grafico_val = np.linspace(-2, 6, 10000)
#  Montar o grafico funcao



#pl.plot(1.73205080756888, fx(1.73205080756888), 'ro')


#pl.plot(xval, fx(xval), 'ro') # pontos resp

pl.plot(grafico_val, fx(grafico_val))



print(f"Raiz raphson {round(vety[interacao-1], 5)}")

#print("Raiz da funcao {}".format(solve(N(fx(x)))))
#pl.show()
