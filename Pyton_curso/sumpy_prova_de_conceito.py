from sympy import *
import numpy as np

# Montar a matriz de jacobiana


# Declarando variaveis algebricas em uma lista e fazendo uma delas virar uma constante e derivar

list_x = []

list_x.append(Symbol('x'))
list_x.append(Symbol('y'))


f = list_x[0]**2+list_x[1]
fx = lambdify(list_x[0], f, modules=['numpy'])

d = diff(fx(list_x[0]).subs(list_x[1], 1), list_x[0])
df = lambdify(list_x[0], d,  modules=['numpy'])
#print(d)



# Declarar variaveis algebricas com nomes variaveis como x1 ... xn
# juntando instrings
inn = 1
i = str(inn)
testa = "x"+i
#print(testa) strings gerada


# Declarar variaveis algebricas com nomes variaveis como x1 ... xn
list_x = []  # zerando lita
quantidade_xn = 5  # x1 e x2

for i in range(quantidade_xn):
    list_x.append(Symbol("x"+str(i)))
#print(list_x) # vetor de variaveis

# Derivar dizendo que somente x0 e variavel e o resto e constantes

deriva_em_funcao_x = 2
f = list_x[0]**2 + list_x[1] + list_x[2]**3
print(f"A funcao: {f}")
print(f"Derivando em : x{deriva_em_funcao_x}")
fx = lambdify(list_x[deriva_em_funcao_x], f, modules=['numpy'])

d = diff(fx(list_x[deriva_em_funcao_x]).subs((list_x[0], list_x[1]), (1, 1)), list_x[deriva_em_funcao_x])

print(f"Resp: {d}")

# Derivar dizendo que somente x0 e variavel e o resto e constantes usanodo lista

deriva_em_funcao_x = 2
f = list_x[0]**2 + list_x[1] + list_x[2]**3
print(f"A funcao: {f}")
print(f"Derivando em : x{deriva_em_funcao_x}")
fx = lambdify(list_x[deriva_em_funcao_x], f, modules=['numpy'])

aux_x = list_x
aux_x.pop(deriva_em_funcao_x)
contantes_x = 1, 1

d = diff(fx(list_x[deriva_em_funcao_x]).subs((aux_x), contantes_x), list_x[deriva_em_funcao_x])

print(f"Resp2: {d}")



# começo

qtd_funcoes = 2  # f1 e f2
qtd_x = 2        # x1 e x2

# iniciando quantidade de x
list_x = []  # zerando lita
funcoes = []

for i in range(qtd_x):
    list_x.append(Symbol("x"+str(i)))

# hummm
funcoes.append(list_x[0] + list_x[1] - 3)

fx = lambdify(list_x[0], funcoes[0], modules=['numpy'])  #  F x0
d = diff(fx(list_x[0]).subs(list_x[1], 1), list_x[0])  # D x0


fx1 = lambdify(list_x[1], funcoes[0], modules=['numpy']) # F x1
d1 = diff(fx1(list_x[1]).subs(list_x[0], 1), list_x[1]) # D x1

print(f"{d} {d1}")

funcoes.append(list_x[0]**2 + list_x[1]**2 - 9)

fx = lambdify(list_x[0], funcoes[1], modules=['numpy'])  #  F x0
d = diff(fx(list_x[0]).subs(list_x[1], 1), list_x[0])  # D x0


fx1 = lambdify(list_x[1], funcoes[1], modules=['numpy']) # F x1
d1 = diff(fx1(list_x[1]).subs(list_x[0], 1), list_x[1]) # D x1


print(f"{d} {d1}")

#  Matriz jacobe for
jacobi = []
aux_x = list_x
print(aux_x)
aux_x.pop(0)
print(aux_x)

# caso precise
eps = 1.0
while eps + 1 > 1:
    eps /= 2

eps *= 2

