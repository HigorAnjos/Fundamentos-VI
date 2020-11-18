from sympy import *
def Epsilon():
    eps = 1.0
    while eps + 1 > 1:
        eps /= 2
    eps *= 2
    return eps


def aureat(ponto_x, d, f, a=-10, b=10):
    x = Symbol('x')
    y = Symbol('y')

    t1 = 0
    t2 = 0
    y1 = 0
    y2 = 0
    while (b - a) > (Epsilon() * 2):
        t1 = a + 0.38 * (b - a)
        t2 = a + 0.62 * (b - a)
        y1 = ponto_x + t1 * d
        y2 = ponto_x + t2 * d
        if f.subs(x, y1[0]).subs(y, y1[1]) < f.subs(x, y2[0]).subs(y, y2[1]):
            b = t2
        else:
            a = t1
    t = (a + b) / 2

    return t

