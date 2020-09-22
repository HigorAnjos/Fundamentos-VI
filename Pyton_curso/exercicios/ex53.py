# e palindromo ?

texto = str(input("frase: ")).strip().upper()

palavras = texto.split()
juntando = ''.join(palavras)


for i in range(len(juntando)-1,-1,-1):
    if juntando[i] != juntando[len(juntando)-1-i]:
        break

if i == 0:
    print("Palindromo ")
else: print("Nao palindromo")

