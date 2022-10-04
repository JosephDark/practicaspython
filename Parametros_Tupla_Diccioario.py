#Parametros de tipo tupla *args
#siempre debe iniciarse con un * para indicar que estipo tupla
def promedio (*numeros):
    """
    Recibe un parametro de tipo tupla, de valores numericos
    E imprime su promedio
    """
    promedio = sum(numeros) / len(numeros)
    print("El promedio es: ", promedio)

promedio (4)
promedio(4,5,6)
promedio(1,2,3,4,5,6,7,8,9)

########################################################
def es_numero(titulo,*serie):
    """
    Imprime un titulo
    Verifica si el caracter en el parametro tupla es un numero o no
    """

    print(titulo)
    for i in serie:
        if type(i) == int or i.isdigit():
            print(f"{i} es un numero")
        else:
            print(f"{i} no es un numero")

es_numero("Numeros","1","2","3")
es_numero("Letras","a","b","c")

nombre = "Mezcla"
lista_varios=["a","2",3,"f",5]

#############################################################################
#Parametros tipo diccionario **kwargs keyword arguments
#estos se preceden con 2 asteriscos 

def area(**dato): # **dato es una variable que recibe un diccionario
    """
    Calcula el área de una figura geométrica y la imprime en pantalla
    """

    #Si el diccionario tiene una clave llamada "figura" evalúa el valor de la clave 
    if dato["figura"]=="Rectangulo":
        print(dato["base"]*dato["altura"])#Si el valor de la clave es "Rectangulo" imprime el valor "base" multiplicado por "altura"
    elif dato["figura"]=="Triangulo":
        print(dato["base"]*dato["altura"]/2)#Si el valor de la clave es "Triangulo" imprime el valor de la clave "base" multiplicado por altura entre dos
    elif dato["figura"]=="Circulo":
        print(3.1416*dato["radio"]**2) #Si el valor de la clave es "Circulo" imprime el valor de la clave "radio" multiplicado por 3.1416
    else:
        print("figura desconocida")# Si el valor de la clave no es ninguna de las anteriores, imprime "figura dsconocida"


area(figura="Triangulo", base = 10, altura = 5)
area(figura = "Circulo", radio = 10, color = "rojo")
area(figura = "dodecagono", lado = 10)
