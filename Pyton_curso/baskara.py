import math


A = 10e-8
B = -0.8
C = 10e-8
x1 = ((-B + math.sqrt(B*B - 4*A*C)) / (2*A))
x2 = ((-B - math.sqrt(B*B - 4*A*C)) / (2*A))
print("x1 = {} e x2 = {} ".format(round(x1, 2), x2))

