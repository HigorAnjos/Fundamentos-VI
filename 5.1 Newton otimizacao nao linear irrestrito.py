from FuncoesCauchyNewton import *
from sympy import *
import numpy as np

x = Symbol('x')
y = Symbol('y')

ponto_x = Matrix([1, 0])

f = 1/2*(x - 2)**2 + (y - 1)**2

constante = 1

Matdiff = Matrix([[diff(f.subs(y, constante))], [diff(f.subs(x, constante))]]) # vetor derivada primeira

d = - Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])

Matdiffseg = Matrix([[diff(diff(f.subs(y, constante)).subs(y, constante)), 0], [0, diff(diff(f.subs(x, constante)).subs(x, constante))]])

mat = Matdiffseg.subs(x, ponto_x[0]).subs(y, ponto_x[1])
dk = mat.LUsolve(d)

t = aureat(ponto_x, dk, f)
ponto_x = ponto_x + t * dk

k = 1
valida = Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])

while valida.norm() >= Epsilon():
    d = - Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])
    mat = Matdiffseg.subs(x, ponto_x[0]).subs(y, ponto_x[1])
    dk = mat.LUsolve(d)
    t = aureat(ponto_x, dk, f)
    ponto_x = ponto_x + t * dk
    k+=1
    valida = Matdiff.subs(x, ponto_x[0]).subs(y, ponto_x[1])

print(f'Newton Min = ({ponto_x[0]}, {ponto_x[1]}) iteracao = {k}')




