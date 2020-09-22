#  ler primeiro termo de uma PA
#  ler a razao
#  imprima os 10 primeiro

a0 = float(input("Digite o primeiro termo: "))
razao = float(input("Digite a Raxzao: "))
aux = a0*razao
for i in range(1, 10+1):
    print(f"a{i+1} = {aux}")
    aux *= razao