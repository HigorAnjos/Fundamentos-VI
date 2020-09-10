numero = ("zero", "um", 'dois', 'trez', 'quatro', 'cinco', 'seis', ' sete', 'oito', 'nove', 'dez')


while (True):
    num = int(input("Digite o numero entre 0 e 10: "))
    if 0 <= num <=10:
        print("voce digitou {}".format(numero[num]))
    if num == -1:
        break
