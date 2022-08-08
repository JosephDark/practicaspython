#Tuplas

vocales = ("a", "e", "i", "o", "u")

print(vocales[2])

print(vocales [:3] + vocales[2:])

print(vocales.index("0"))

lista_vocales = list(vocales)  #list convierte una tupla en lista

lista_vocales[2] = "I" #La lista generada a partir de la tupla sí es modificable.

print(lista_vocales) 

tupla_vocales = tuple(lista_vocales) #Para convertir una lista en tupla se usa tuple

###########################################################
#CONJNTOS

canasta = {"manzana", "pera", "manzana", "pera", "naranaja", "platano"}

print(canasta)

print("manzana" in canasta) #Arroja el valor bool de True porque sí esta en canasta
print("melon" in canasta)   #Arroja el valor false porque no esta en canasta

vocales = ["a", "e", "i", "o", "u", "a"]

print(vocales)

vocales = list(set(vocales))

vocales1 = {"a", "e", "i", "o","u","a"}
vocales2 = {"e", "i", "o"}

print(vocales2.issubset(vocales1))  ##Revisa si vocales2 es subconjunto de vocales1

print(vocales2 - vocales1)  #Diferencia de Conjuntos
print(vocales2 | vocales1)  #Union de conjuntos
print(vocales2 & vocales1)  #Interseccion
print(vocales2 ^ vocales1)  #Diferencia simetrica 

#################################################################
#Diccionarios

tiempos = {
    "Hamilton" : "1.49",
    "Bottas"  : "1.56",
    "Perez"  : "1.53",
    "Verstappen" : "1.52"

}

print(tiempos.items())  #Descompone el diccionario en tupplas
print(tiempos.keys())   #obtiene las llaves del disccionario
print(tiempos.values()) #Obtiene los valores del diccionario

print(tiempos.get("Hamilton")) #Para obtener el valor de una llave
print(tiempos.get("amilton", "No encontrado")) # Permite usar un mensaje personalizado

tiempos = dict(
    Hamilton = "1:14.6",
    Bottas = "1:56.3",
    Perez = "1_53.8",
    Verstappen = "1:52.6"
)