import numpy as np
import math

ponto = 1.3

x_valores = np.array([1.3, 1.5, 2])
y_fx = np.array([2.497, 3.875, 9])


matriz = np.zeros(shape=(len(x_valores), len(y_fx)))


for i in range(len(x_valores)):
    for j in range(len(x_valores)):
        matriz[i][j] = float(x_valores[i]**j)

x = np.linalg.solve(matriz, y_fx)
print(x)
resp = 0

for i in range(0, len(x)):
    resp += x[i]*(ponto)**i


print(round(resp, 3))