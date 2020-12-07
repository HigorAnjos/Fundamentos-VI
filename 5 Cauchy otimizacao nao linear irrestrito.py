from FuncoesCauchyNewton import *
from sympy import *
import numpy as np
eps = Epsilon()

x = Symbol('x')
y = Symbol('y')

ponto_x = Matrix([1, 0])
f = 1/2*(x - 2)**2 + (y - 1)**2

constante = 1
Matdiff = Matrix([[diff(f.subs(y, constante))], [diff(f.subs(x, constante))]]) # vetor derivada primeira

d = - Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])

#print(f'M = {Matdiff}')
#print(f'd = {Matdiff}')

t = aureat(ponto_x, d, f)
#print(f' t = {t}')


ponto_x = ponto_x + t * d

#print(ponto_x)
k = 1


validacao = Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])

while validacao.norm() >= Epsilon():
    d = - Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])
    t = aureat(ponto_x, d, f)
    ponto_x = ponto_x + t * d
    k = 1 + k
    validacao = Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])


print(f'Cauchy Min = ({ponto_x[0]}, {ponto_x[1]}) iteracao = {k}')

