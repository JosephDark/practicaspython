vocales = ["a", "e", "i", "o", "u"]
print(vocales)

vocales[1:4] = ["E", "I", "O"]   #Inserta estos nuevos elementos en lugar de los elementos de las posiciones de la 1 a la 3
print(vocales)

print (vocales, len(vocales))

vocales [1:4] = []     #Borramos los elementos de la posicion 1 a 3
print(vocales)

vocales[1:2]=["e", "i", "o", "u"] #insert valores a patri de la posicion 1
print (vocales, len(vocales))

vocales.extend(["i", "i"])  #Extiende la lista con elementos nuevos al final de esta. 
print (vocales, len(vocales))

print(vocales.index("i"))  #Busca la primera aparición de i en la lista 

print(vocales.count("i")) #cuenta cuantas veces aparece i dentro de la lista

print(vocales.index("i",4))   #Busca i a partir d la posicion 4 de la lista

#############################################################################

carros= ["Audi", "Ford", "BMW", "VW"]

carros.sort(key=len) #ordena por longitud de caracteres y en segundo lugar, por alfabeto.

print(carros)

###############################################################################

listas = [[0,1],[2, 3, 4],[5, 6]]

print(listas[0], listas[1:3]) #Imprime la lista de indice 0, despues las listas de subidice 1 a 3

print(listas[2][1])  #Imprime la lista2, el elemento 1

###############################################################################

vocales1 = ["a","e","i","o","u"]

vocales2 = vocales1 

print(vocales1, vocales2)

print(id(vocales1), id(vocales2)) #Para optimizar memoria, python referencia la variable cuando se "copia"

vocales3 = vocales1.copy() 

