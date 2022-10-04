
import numpy as np
import matplotlib.pyplot as plt
from random import randint

def grafica(carriles2):

    abcisa = []
    for i in range(12):
        abcisa.append(i+1)

    plt.suptitle('Simulacion de la Maquina de Galton')
    #plt.bar(X + 0.00, carril*250)
    plt.bar(abcisa, carriles2,width=1)
    plt.show()


def calculo(niveles,carril ):

    carriles = []
    for i in range(niveles):
        valor = 0
        carriles.append(valor)



    for h in range((carril)*250):
        guarda = -1
        for j in range(carril):
            #stored += randint(0, 1)
            guarda = guarda + randint(0,1)
        carriles[guarda] += 1


    print((niveles)*250, "pelotas")
    print(carriles)
    print (len(carriles))

    # if len(carriles) %2==0:
    #     #X = np.arange(-((len(carriles)/2)-1), (len(carriles)/2)+1)
    #     X = []
    #     for i in range(12):
    #         X.append(i+1)
    # else:
    #     X = np.arange(-((len(carriles)/2)-.5), (len(carriles)/2)+.5)


    grafica(carriles)
    # abcisa = []
    # for i in range(12):
    #     abcisa.append(i+1)

    # plt.suptitle('Maquina de Galton')
    # #plt.bar(X + 0.00, carril*250)
    # plt.bar(abcisa, carriles,width=1)
    # plt.show()


calculo(12,12)
