from cmath import pi


pila = [3, 6, 7]

while len(pila) >= 3:
    if pila [-1] % 3 :               #Pedimos el ultimo elemento de la pila. Inidice negativo es un alista circular 
        extraido = pila.pop()        #Extraemos el último el elemento   
        pila.append(extraido + 1)    #Introducimos a la pila el elelemyo extraido + 1 
        print(pila)                  #Imprimimos la pila 
    else :
        print ("Todos los elementos de la pila son multiplos de 3")
        break
