import matplotlib.pyplot as plt

x = []
y = []

dataset = open('Users/win/Documents/GitHub/Fundamentos-VI/Pyton_curso/lendo_aquivo_csv/dataset.txt','r')

for line in dataset:
    line = line.strip()
    X, Y  = line.split(',')
    x.append (X)
    y.append (Y)

dataset.close()

plt.plot(x, y)

plt.title('exemplot')
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()