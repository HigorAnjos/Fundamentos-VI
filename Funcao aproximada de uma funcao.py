from sympy import *
import numpy as np
import math

# interpolacao Linear

xp = 0.5
pontos_x = np.array([0.1, 0.6])
pontos_fx = np.array([1.221, 3.320])



matriz = list()
for i in range (len(pontos_x)):
    matriz.append([1, pontos_x[i]])

matriz = np.array(matriz)

vetorb = pontos_fx

dim = len(matriz)
D = np.zeros((dim, dim)) # Diagonal
F = np.zeros((dim, dim)) # Triangular_superior
E = np.zeros((dim, dim)) # Triangular_inferior
for i in range(0, len(matriz)):
    D[i][i] = matriz[i][i]


for i in range(0, len(matriz)):
    for j in range(i+1, len(matriz)):
        F[i][j] = matriz[i][j]

for i in range(0, len(matriz)):
    for j in range(0, i):
        E[i][j] = matriz[i][j]

E *= -1  # (-E) pois A = D (-E) -F
F *= -1  # (-F) pois A = D -E (-F)


E_F = E+F
matriz_j = np.linalg.inv(D)   # D^(-1)
matriz_j = matriz_j.dot(E_F)  # matriz_j = np.linalg.inv(D).dot(E_F)

# Temos a matriz de jacob

# calcula o c(e uma constante), c = D^(-1)*b -> c = D^(-1)*vetorb
c = np.linalg.inv(D).dot(vetorb)

# iniciando o x Na origem [0,..,0]
x = np.zeros((dim))

#  primeira interacao
x = matriz_j.dot(x)+c
x_anterior = x
# print(x)

#  segunda interacao
x = matriz_j.dot(x) + c
# print(x)

vetor = np.zeros((dim))

for i in range(0, dim):
    vetor[i] = x[i] - x_anterior[i]

# print(vetor)

modulo = 0

for i in range(0, dim):
   modulo += np.absolute(vetor[i])

modulo = modulo ** (1 / 2)
# print(modulo)
ki = 1
#print(f"primeira interacao {x}")
while modulo > 0.00001:
    modulo = 0
    x_anterior = x
    x = matriz_j.dot(x) + c
    ki+=1
    vetor = np.zeros((dim))
    for i in range(0, dim):
        vetor[i] = x[i] - x_anterior[i]
    for i in range(0, dim):
        modulo += np.absolute(vetor[i])
    modulo = modulo ** (1 / 2)
#print(f"Interacoes {ki}")
#print(np.round(x, 4))


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
x[0] = truncate(x[0], 4)
x[1] = truncate(x[1], 4)
print(f'a = {x[0]}, b = {x[1]}')

print(f'f({xp}) = {truncate(x[0] + x[1]*xp, 4)} ')



