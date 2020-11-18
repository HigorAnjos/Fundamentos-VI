import numpy as np
from sympy import *
from numpy.linalg import solve
import math


x1 = Symbol('x1')
x2 = Symbol('x2')
# Ponto de inicio do x0
x = np.array((1, 5))

# Partir da matriz de jacob
fx1 = x1 + x2 - 3
fx2 = x1**2 + x2**2 - 9



f1 = lambdify(x1, fx1, modules=['numpy'])
f2 = lambdify(x1, fx2, modules=['numpy'])



# jacobiana
# A B
# C D

#   F1
# f2 derivada em x1
D_x1 = diff(f1(x1).subs(x2, 1), x1)
f1_d_x1 = lambdify(x1, D_x1, modules=['numpy'])

f1_aux = lambdify(x2, fx1, modules=['numpy'])

# f2 derivada em x2
D_x2 = diff(f1_aux(x2).subs(x1, 1), x2)
f1_d_x2 = lambdify(x2, D_x2, modules=['numpy'])

#print(f"{D_x1} {D_x2}")

#   f2
# f2 derivada em x1
D_x1 = diff(f2(x1).subs(x2, 1), x1)
f2_d_x1 = lambdify(x1, D_x1, modules=['numpy'])  # chama f1_d_x1 para passar o valor de x1 em funcao f1 devirada em x1

f2_aux = lambdify(x2, fx2, modules=['numpy'])

# f2 derivada em x2
D_x2 = diff(f2_aux(x2).subs(x1, 1), x2)
f2_d_x2 = lambdify(x2, D_x2, modules=['numpy'])  # chama f1_d_x1 para passar o valor de x1 em funcao f1 devirada em x1

#print(f"{D_x1} {D_x2}")

jacobiana = np.array(([float(f1_d_x1(x[0])), float(f1_d_x2(x[1]))],
                      [float(f2_d_x1(x[0])), float(f2_d_x2(x[1]))]))

vetor_f_x = np.array((float(f1(x[0]).subs(x2, x[1])), float(f2(x[0]).subs(x2, x[1]))))
#print(vetor_f_x) # F(x0)

s0 = np.linalg.solve(jacobiana, -vetor_f_x)

x = x + s0
print(f"Primeira interacao {x}")
intecacoes = 1
vetor_f_x = np.array((float(f1(x[0]).subs(x2, x[1])), float(f2(x[0]).subs(x2, x[1]))))
while np.linalg.norm(vetor_f_x) >= 0.00001:
    jacobiana = np.array(([float(f1_d_x1(x[0])), float(f1_d_x2(x[1]))],
                          [float(f2_d_x1(x[0])), float(f2_d_x2(x[1]))]))

    s0 = np.linalg.solve(jacobiana, -vetor_f_x)
    x = x + s0
    vetor_f_x = np.array((float(f1(x[0]).subs(x2, x[1])), float(f2(x[0]).subs(x2, x[1]))))
    intecacoes += 1

##
def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
##

print(f"Resposta [{truncate(x[0], 4)}, {truncate(x[1], 4)}] interacoes {intecacoes}")

