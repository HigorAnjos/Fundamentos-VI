# Instroducao a plotagem de grafico


import numpy as np
import matplotlib.pyplot as plt

y = np.array([1, 2, 3, 5])
x = np.array([1, 2, 3, 5])
plt.stem(x, y)

plt.title("seno")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.grid(True)

plt.show()

# Fazer um grafico com dados do menor numero epsilon
# grafico com a funcao da prova