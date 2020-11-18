from sympy import *

x = Symbol('x')
#x**4-1/3*x**3-3/2*x**2
f = 1/2*x**2+1/4*x**4-1/2*x**2
fx = lambdify(x, f, modules=['numpy'])
df = diff(fx(x), x)
dfx = lambdify(x, df, modules=['numpy'])
raiz_primeira_df = solve(df)

segunda_df = diff(dfx(x), x)
seg_dfx = lambdify(x, segunda_df, modules=['numpy'])

print(f'Raizes da primeira derivada {raiz_primeira_df} \n')


for i in range(len(raiz_primeira_df)):
    if seg_dfx(raiz_primeira_df[i]) > 0:
        print(f"Min f({raiz_primeira_df[i]}) = {seg_dfx(raiz_primeira_df[i])}")
    if seg_dfx(raiz_primeira_df[i]) < 0:
        print(f"Max f({raiz_primeira_df[i]}) = {seg_dfx(raiz_primeira_df[i])}")
    if  seg_dfx(raiz_primeira_df[i]) == 0:
        print(f"Indefinido f({raiz_primeira_df[i]}) = {seg_dfx(raiz_primeira_df[i])}")

raizes_segunda_df = solve(seg_dfx(x))

print(f'\nPontos de inflexao (Muda a concavidade)')
#CARMEN CECÍLIA CENTENO
#99652-7542


for i in range(len(raizes_segunda_df)):
    print(f'Pontos = (({raizes_segunda_df[i]}), f({fx(raizes_segunda_df[i])}))')

print(solve(1/2*(1-x)**2*(1)**2))