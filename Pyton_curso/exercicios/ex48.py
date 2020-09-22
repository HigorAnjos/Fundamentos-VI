#  Soma de todos impares e multiplos 3 no intervalo de 1 a 500
soma = 0
for i in range(1, 500):
    if i % 2 == 1:
        if i % 3 == 0:
            soma+= i
print(soma)
