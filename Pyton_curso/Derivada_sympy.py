#  1 Calcular derivada
from sympy import *
from numpy import linalg

#  equacao de primerio grau
x = Symbol('x')
#  2x+5=0
resposta = solve(2*x+5, x)
print(resposta)

#  2x² – 3x + 1

resultado = solve(2*x**2-3*x+1, x)
print(resultado)
#  Deriva a funcao 2*x**2-3*x+1 -> 2x² – 3x + 1
#  Pega a expressao
#  substitui o valor de x por 1, 2, 3

f = Lambda(x, (2*x**2-3*x+1) )
derivada = diff(f(x), x)
print(derivada)


N = 1
x1 = diff(f(x),x).subs(x,N)
print(f"f'({N}) igual a 1 = Y = {x1}")
N = 2
x1 = diff(f(x),x).subs(x,N)
print(f"f'({N}) igual a 1 = Y = {x1}")
N = 3
x1 = diff(f(x),x).subs(x,N)
print(f"f'({N}) igual a 1 = Y = {x1}")

# plot(f(x), (x, -2, 2))

Derivada_igual_a_0 = solve(diff(f(x), x), x)
print(f"Derivada igual a zero {Derivada_igual_a_0}")
#  Pegar a raiz da derivada e por em um float






#  Testando a prova, segundo grau.
#  10**-8*x**2-0.8x+10**-8

resposta = solve(10**(-8)*x**2-0.8*x+10**-8, x)
print(resposta)

#  plot(x+2, (x, -10, 10))



