import random
import matplotlib.pyplot as plt

eje_x = [random.randint(1,100) for n in range(100)] #Compresion de listas para generar una lista de valores de X
eje_y = [random.randint(1,100) for n in range(100)] #Compresion de listas para generar una lista de valores de y

plt.scatter(eje_x,eje_y) #Scatter hace parejas de doordenadas

plt.title("Grafica de dispersion")

plt.show()