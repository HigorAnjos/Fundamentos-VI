#  e primo?

num = int(input("Numero: "))

for i in range(2, num):
    if num % i == 0:
        break


if(i == num-1):
    print("Primo!")
else: print("Nao e primo!")