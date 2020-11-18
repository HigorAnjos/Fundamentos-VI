import numpy as np


matriz = np.array(([10, 3, -2],
                   [2, 8, -1],
                   [1, 1, 5]))

vetorb = np.array(([57, 20, -4]))

# 1x + 1y = 3
# 1x - 3y = -3


# Decompor a Matriz, Identidade(D), Triangular_inferior(E), Triangular_superior(F)
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
print(f"Interacoes {ki}")
print(np.round(x, 4))