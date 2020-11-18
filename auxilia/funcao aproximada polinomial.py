import numpy as np
import math

ponto = 0.2

x_valores = np.array([0.1, 0.6, 0.8])
y_fx = np.array([1.221, 3.320, 4.953])


matriz = np.zeros(shape=(len(x_valores), len(y_fx)))


for i in range(len(x_valores)):
    for j in range(len(x_valores)):
        matriz[i][j] = float(x_valores[i]**j)

x = np.linalg.solve(matriz, y_fx)

resp = 0

for i in range(0, len(x)):
    resp += x[i]*(ponto)**i


print(round(resp, 3))