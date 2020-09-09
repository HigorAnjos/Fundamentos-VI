import numpy as np

a = np.array([1, 2, 3])

print("Valor {} \nTipo {}".format(a, type(a)))

print(a[0])
print(a[-3])
print(a.ndim)  # Numero de dimensoes

#  Duas linhas

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print("Numero de dimensoes b -> {}".format(b.ndim))
print("Dimensao do array b Linha Coluna {}".format(b.shape))
print(len(b))  # Quantidade de elementos em b

