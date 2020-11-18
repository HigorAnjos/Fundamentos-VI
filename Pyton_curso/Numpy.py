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

# Criando vetor com funcoes

c = np.arange(10, 20)
print("vet C{}".format(c))

d = np.linspace(1, 10, 10)
print(d)

# vetor Matriz com 1 e 0 e random

e = np.ones(10)
print(e)
e = np.zeros(10)
print(e)
e = np.ones((2, 3))
print(e)

e = np.random.rand(5)
print("\n{} ".format(e))
e = np.random.rand(2, 3)
print("\n\n{} ".format(e))

# Matriz identidade

f = np.eye(3)
print("\n\n{} ".format(f))
f = np.diag(np.array([1, 2, 3, 4]))
print("\n\n{} ".format(f)) # insere ^aqueles elementos na diagonal

# Sub array

g = np.arange(10, 21)
print(g)
print(g[2:5])

# atividade Selecionar matriz
