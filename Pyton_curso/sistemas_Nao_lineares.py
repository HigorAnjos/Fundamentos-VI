import numpy as np
from sympy import *
from numpy.linalg import solve

x1 = Symbol('x1')
x2 = Symbol('x2')

# Partir da matriz de jacob
fx1 = x1 + x2 - 3
fx2 = x1 ** 2 + x2 ** 2 - 9

f1 = lambdify(x1, fx1, modules=['numpy'])
f2 = lambdify(x1, fx2, modules=['numpy'])

x = np.array((1, 5))

jacobiana = np.array(([1, 1],
                      [2, 2]))

# F(x0)
F_x = np.array((float(f1(x[0]).subs(x2, x[1])),
                float(f2(x[0]).subs(x2, x[1]))))

jacobiana[1][0] = jacobiana[1][0] * x[0]
jacobiana[1][1] = jacobiana[1][1] * x[1]

s0 = np.linalg.solve(jacobiana, -F_x)

x = x + s0 # x1

print(np.linalg.norm(F_x))
print(x)
for i in range(15):
      F_x = np.array((float(f1(x[0]).subs(x2, x[1])),
                      float(f2(x[0]).subs(x2, x[1]))))

      jacobiana[1][0] = jacobiana[1][0] * x[0]
      jacobiana[1][1] = jacobiana[1][1] * x[1]

      s0 = np.linalg.solve(jacobiana, -F_x)
      x = x + s0
      print(x)

print(np.linalg.norm(F_x))
print(np.linalg.norm(x))

