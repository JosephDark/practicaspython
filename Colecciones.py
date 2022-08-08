mix= [0, 1.0, "dos", 3 + 4j]

print(len(mix)) #imprime el tamaño de la lista

for i in mix :
    print(f"{i:6} - Tipo: {type(i)}")


sin_dos = mix[:2] + mix [3:] #concatenamos piezas de la lista 

print(mix, sin_dos) 

duplicado = mix * 2  #duplica la lista por dos

print(duplicado) 


cuadrados = [0, 1, 4, 9, 16, 25]

for i in range(len(cuadrados)):            #Recorre la lista imprimiendo los elementos de la lista cuadrados
    print(f"{i}**2 = {cuadrados[i]}")


for i in range(len(cuadrados)):            #Recorre la lista imprimiendo los elementos de la lista cuadrados y multiplicandolos
     cuadrados[i] = cuadrados[i] * i        #por si mismos una vez para hacerlos cubos 
     print(f"Ahora están al cubo = {cuadrados[i]}")

cuadrados.append(7 ** 3)    #cincluye elemento al final de la lista
print(cuadrados)
cuadrados.insert(6, 6 ** 3) #inserta un elemento en la posicion deseada, en este caso en la seis
print(cuadrados)
cuadrados.extend([27, 1000, -1])   #Inserta multiples elementos al final de la lista 
print(cuadrados)
del cuadrados[9:]   #Elimina de la posición 9 en adelante
print(cuadrados)
cuadrados.remove(27)  #elimina la parimera aparicion del 27 en la lista
print(cuadrados)

valor_removido = cuadrados.pop(2)
print(valor_removido)

cuadrados.clear()
