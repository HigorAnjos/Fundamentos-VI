from sympy import *
import numpy as np
x1 = Symbol('x1')
x2 = Symbol('x2')

ponto_x = Matrix([1, 0])

f = 1/2*x1**2+1/4*x2**4-1/2*x2**2

constante = 1
Matdiff = Matrix([[diff(f.subs(x2, constante))], [diff(f.subs(x1, constante))]]) # vetor derivada primeira
Matdiffseg = Matrix([[diff(diff(f.subs(x2, constante)).subs(x2, constante)), 0], [0, diff(diff(f.subs(x1, constante)).subs(x1, constante))]]) # Matriz quadrada derivada seg


print(Matdiff)
d = - Matdiff.subs(x1, ponto_x[0]).subs(x2, ponto_x[1])
t = 1
print(f'Direcao {d}')

novo_x = ponto_x + t * d
ponto_x = novo_x
#print(f.subs(x1, novo_x[0]).subs(x2, novo_x[1]))

print(f't = {t}')

validacao = Matdiff.subs(x1, novo_x[0]).subs(x2, novo_x[1])
k = 1

while validacao.norm() >= 0.001:
    d = - Matdiff.subs(x1, ponto_x[0]).subs(x2, ponto_x[1])
    novo_x = ponto_x + 1 * d
    validacao = Matdiff.subs(x1, novo_x[0]).subs(x2, novo_x[1])


    k = k + 1
    ponto_x = novo_x + d
    print(f'Min = ({novo_x[0]}, {novo_x[1]}), iteracao = {k}')


print(f'Min = ({novo_x[0]}, {novo_x[1]}), iteracao = {k}')
