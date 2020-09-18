from sympy import *

x = Symbol('x')
f = Lambda(x, (x/(x+1)))
vet = [-3, -2, 0, 0.75, 1, 2, 3, 4]
for i in range(len(vet)):
     print("({}, {})".format(vet[i], f(x).subs(x, vet[i])))

plot(3, f(3))


