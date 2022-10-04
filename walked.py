import random
import numpy as np
import matplotlib.pyplot as plt

#Probabilidad de ir arriba o abajo
prob=[0.05,0.95]

#estadisticamente estableciendo la posicion de inicio
start = 2
positions = [start]

#Creando los puntos aleatorios
rr = np.random.random(1000)
downp = rr < prob[0]
upp = rr > prob[1]

for idownp, iupp in zip(downp, upp):
    down = idownp and positions[-1]>1
    up = iupp and positions[-1] < 4
    positions.append(positions[-1] - down + up)



print(positions[:10])
print(downp[:10])
print(upp[:10])
print(positions[-1])
print(down)
print(up)
#Graficando
plt.plot(positions)
plt.show()