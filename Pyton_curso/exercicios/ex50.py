#  ler 6 inteiros
#  Soma dos pares
soma = 0
for i in range(1, 7):
    lido = int(input("Digite um valor "))
    if lido % 2 == 0:
        soma += lido
print(soma)