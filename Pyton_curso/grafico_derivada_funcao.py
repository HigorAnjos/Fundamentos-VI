import matplotlib.pyplot as plt

# list.append(x) acrescentar itens

valores_para_x = [ -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6.1, 7, 8, 9, 10]
y = []
for num in range(len(valores_para_x)):
    y.append((valores_para_x[num] + 6) / (valores_para_x[num] * valores_para_x[num] - 36))
    print(num)

plt.plot(valores_para_x, y)
plt.show()

# ficou ruim, nao consigo visualizar o mais infinito e menos infinito
