# cuadrados =[]

# for numero in range (10):
#     numero= numero **2
#     cuadrados.append(numero)
# print(cuadrados)
# print(numero)

# cubos = [cubo**3 for cubo in range(10)] #compresion de lista, se definen los elementos de la lista 
# print (cubos)                           #mediante un ciclo.

#############################################################################3
#Compresion de un diccionario por medio de la compresion de listas
# cubos = {numero : numero **3 for numero in range (10)} #se define la llave y su valor por medio de un ciclo
# print(cubos)

#Tambien se pueden usar condicionales en las definicion de la compresion de listas 
#en el siguente caso se discrimina si el numero es par o impar mediante if y la division por modulo 2
# pares =[numero for numero in range (1,11) if numero % 2 == 0]
# impares = [numero for numero in range (1,11) if numero % 2 != 0]
# print(pares)
# print(impares)

#una lista puede modificarse mediante la compresion de listas 
nombres = ["ana","carlos","fernando","xochitl"]
print ("Lista antes de la compresion de lista:", nombres)
nombres =[nombre.capitalize() for nombre in nombres]
print("Lista después de la compresion:", nombres)

#todo esto nos ayuda a ahorrar memoria en uso, programas más cortos y menos codigo

frase = input ("Escribe una frase:")
frase = frase.lower()
palabras = frase.split()

respuesta =" "

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + " "
    else :
        respuesta = respuesta + palabra + " "

print(respuesta)
