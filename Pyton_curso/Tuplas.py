# () Tupa [] Lista {} Dicionario
#  Tuplas sao imutaveis

lanche = ("sanduiche", "suco", "pizza", "pudim")
print(lanche)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'eu vou come {comida}')

for i, comida in enumerate(lanche):
    print(f'eu vou come {comida} na posicao {i}')

print(sorted(lanche))  # ordenado

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 7)

c = a+b
print(c)
print(c.count(7))
c = b+a
print(c)
print(c.index(7))
print(c.index(7, 2))


