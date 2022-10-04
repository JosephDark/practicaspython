while True:           #Usamos un ciclo para validar el dato ingresado mediante el error generado
    try:              #via la conversion usando int,mediante la estructura Try except
        coordenadaX =int(input("Ingrese el valor de la cooordenada X: ")) 
        if coordenadaX == 0:                      #si no genera error, validamos si el valor es 0, 
            print("El valor de X no puede ser 0")
        elif coordenadaX < 0:
            print("El valor de X es negativo")     #si el numero es negativo
            break
        elif coordenadaX > 0:
            print("El valor de X es positivo")     #o si es positivo. Ambos casos sacan del ciclo.
            break

    except:   #Si se genera el error, se maneja aqui y se avisa que el valor no es válido. Reinicia.
         print("No has ingresado un numero valido para la coordenada X")


while True:     #Ejecuta la misma validacion para la coordenada Y
    try:
        coordenadaY =int(input("Ingrese el valor de la cooordenada Y: "))
        if coordenadaY == 0:
            print("El valor de Y no puede ser 0")
        elif coordenadaY < 0:
            print("El valor de Y es negativo")
            break
        elif coordenadaY > 0:
            print("#El valor de Y es positivo")
            break

    except:
         print("No has ingresado un numero valido para la coordenada Y")


coordenada = [coordenadaX, coordenadaY] #Ingresamos los valores en una lista, para un par ordenado

#El par ordenado es evaluado en su valor numerico para determinar el cuadrante correspondiente.
if coordenada[0] > 0 and coordenada[1] > 0 :
    print("El punto se encuentra en el Cuadrante I")
elif coordenada[0] < 0 and coordenada[1] > 0 :
    print("El punto se encuentra en el Cuadrante II")
elif coordenada[0] < 0 and coordenada[1] < 0 :
    print("El punto se encuentra en el Cuadrante III")
elif coordenada[0] > 0 and coordenada[1] < 0 :
    print("El punto se encuentra en el Cuadrante IV")
