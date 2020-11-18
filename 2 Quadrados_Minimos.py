import numpy as np
import matplotlib.pyplot as plt

xi = np.array((-1, 0, 1, 2, 3, 4, 5, 6))
yi = np.array((10, 9, 7, 5, 4, 3, 0, -1))
n = len(xi)

xi2 = np.ones(n)
xy = np.ones(n)

for i in range(n):
    xi2[i] = xi[i]** 2
    xy[i] = xi[i] * yi[i]


def somatorio(x):
    soma = 0
    for i in range(len(x)):
        soma += x[i]
    return soma

#(somatorio(xi), somatorio(yi), somatorio(xi2), somatorio(xy))

s = np.ones(4)

s[0] = somatorio(xi)
s[1] = somatorio(yi)
s[2] = somatorio(xi2)
s[3] = somatorio(xy)

mat = np.ones((2, 2))
b = np.array((s[3], s[1]))

mat[0][0] = s[2]
mat[0][1] = s[0]

mat[1][0] = s[0]
mat[1][1] = n


x = np.linalg.solve(mat, b)
print(f'a = {x[0]}, b = {x[1]}')

########################### plotando os pontos
#### y = ax+b
plt.plot(xi, yi, 'ro')

d = np.linspace(-2, 7, 10)
dx = np.ones(10)

for i in range(len(d)):
    dx[i] = x[0]*d[i] + x[1]

plt.plot(d, dx)
plt.show()