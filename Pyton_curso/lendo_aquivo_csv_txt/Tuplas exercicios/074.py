from random import randint

n = (randint(1, 100), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)

print("Maior {}, Menor {} ".format(max(n), min(n)))