from sympy import *
from numpy import *

x = Symbol('x')

ponto_x = 4
# Pn -> Polinomio de grau n
vet_x = array([0, 1, 2, 3, 4])
vet_y = array([32, 47, 65, 92, 132])


def L(vet_x, vet_y, ponto_x):
    l = list()
    aux_Numerado = 1
    aux_den = 1
    for k in range(len(vet_x)):
        for j in range(len(vet_x)):
            if k != j:
                aux_Numerado *= float(ponto_x - vet_x[j])
        for j in range(len(vet_x)):
            if k != j:
                aux_den *= float(vet_x[k] - vet_x[j])
        l.append(aux_Numerado / aux_den)
        aux_Numerado = 1
        aux_den = 1
    return l

l = L(vet_x, vet_y, ponto_x)
aux = 0
for k in range(len(vet_y)):
     aux += (vet_y[k] * l[k])

print(f"Resp: {aux}")





# qual e a funcao de cada L
aux_Numerado = 1
aux_den = 1
l = list()
for k in range(len(vet_x)):
    for j in range(len(vet_x)):
        if k != j:
            aux_Numerado *= (x - vet_x[j])
    for j in range(len(vet_x)):
        if k != j:
            aux_den *= (vet_x[k] - vet_x[j])
    l.append(aux_Numerado / aux_den)
    aux_Numerado = 1
    aux_den = 1

# print(l[1]) Aqui da a funcao de cada L[n]
