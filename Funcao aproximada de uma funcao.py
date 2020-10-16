from sympy import *
import numpy as np

x = Symbol('x')

# Funcao "dificil" pra usar
f = x**4-12*x**3+47*x**2-60*x

fx = lambdify(x, f, modules=['numpy'])
pontos_fx = np.array([fx(2), fx(10/3)])

print(pontos_fx, fx(-5))

# a + b*(2) = -12
# a + b*(10/3) = 1.2345679


# a = -31.8519
# b = 9.9259

#portanto  a + bx