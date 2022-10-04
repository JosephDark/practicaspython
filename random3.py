import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) #Semilla del random

numeros = np.random.rand(10) #numeros de aleatorios que queremos

print(numeros)

plt.plot(numeros)
plt.show()

