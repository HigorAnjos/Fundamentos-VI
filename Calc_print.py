from sympy import *
import numpy
init_printing()

x = Symbol('x')
f = x**2 -4
f = lambdify(x, f, modules=['numpy'])
n = 16
partes = 4/n
aux = 0

for i in range(n):
    print(f'{i+1}ª parte de {nsimplify(aux)} a {nsimplify((i+1)*partes)}')
    aux = aux + partes

print(f'Pontos Medios')
aux = 0
pontost = list()

for i in range(n):
    print(f't{i+1} = ({nsimplify(aux)} + {nsimplify((i+1)*partes)}) / 2 = { nsimplify((aux+(i+1)*partes)/2)}')
    pontost.append(nsimplify((aux + (i + 1) * partes) / 2))
    aux = aux + partes


print(f'Calculando a area')

linha =''
area_igual = 0
for i in range(n):
    #print(f'{nsimplify(partes)} * f({pontost[i]}) +')
    linha += f'{nsimplify(partes)} * f({pontost[i]}) + '
    area_igual += nsimplify(partes)*f(pontost[i])
print(f'Area = {linha} = {nsimplify(area_igual)} ------- {float(area_igual)}')
