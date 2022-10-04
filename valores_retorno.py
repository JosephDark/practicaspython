def promedio (*numeros):
    """Funcion que calcula el promedio de una serie 
    y regresa el valor al ámbito principal"""
    return sum(numeros)/len(numeros) #Return nos indica que la funcion debe reresar este valor
                                    # al ambito principal y termina la ejecucion de la funcion.
x = promedio(4,5,6)
print(x)


#Valores de Retorno sentencia return
def area(**dato): # **dato es una variable que recibe un diccionario
    """
    Calcula el área de una figura geométrica y la imprime en pantalla
    """

    #Si el diccionario tiene una clave llamada "figura" evalúa el valor de la clave 
    if dato["figura"]=="Rectangulo":
        return (dato["base"]*dato["altura"])#Si el valor de la clave es "Rectangulo" imprime el valor "base" multiplicado por "altura"
    elif dato["figura"]=="Triangulo":
        return(dato["base"]*dato["altura"]/2)#Si el valor de la clave es "Triangulo" imprime el valor de la clave "base" multiplicado por altura entre dos
    elif dato["figura"]=="Circulo":
        return(3.1416*dato["radio"]**2) #Si el valor de la clave es "Circulo" imprime el valor de la clave "radio" multiplicado por 3.1416
    else:
        print("figura desconocida")# Si el valor de la clave no es ninguna de las anteriores, imprime "figura dsconocida"


triangulo = area(figura="Triangulo", base = 10, altura = 5)
print(f"El area del triangulo es {triangulo}")
circulo = area(figura = "Circulo", radio = 10, color = "rojo")
print(f"El area del circuko es {circulo}")
dodecagono = area(figura = "dodecagono", lado = 10)
print(f"El area del docecagono es {dodecagono}")

##########################################################################
#Recursividad de funciones de python
#Limite por default de las recursiones es 996 recursiones
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

print("El factorial de 0 es (0!):",factorial(0))
print("El factorial de 0 es (1!):",factorial(1))
print("El factorial de 0 es (3!):",factorial(3))

##########################################################################3
#Funciones Lambda o funciones anonimas.
#Son funciones sencillas que se usan de auxiliares dentro de otras funciones

suma = lambda x,y : x + y    #Definicion de la funcion es parametros : cuerpo de la funcion
print(suma("Hola ", "mundo!"))#Utilizacion de la funcion
print(suma(2,5))

lista_numeros =[1, 0 , -2]
lista_numeros = sorted(lista_numeros, key= lambda n: abs(n)) #F. Lambda en el parametro de orden de sorted
print(lista_numeros)

############################################################################
# Funcion Zip
#Concatena elementos de varias listas con el mismo indice, cuantas veces tenga elementos la menor 
#de las listas concatenadas. Generalmente se usa con el ciclo for
paises=["Kenia", "Francia", "Mexico", "Tokio"]
capitales=["Nairobi","Paris","Ciudad de Mexico"]
poblacion=[54,66,130]

for i in zip(paises,capitales,poblacion):
    print(i)