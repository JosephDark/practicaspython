#Manejo de errores 

denominador = 10
numerador = 0
cadena = "3"
numerico = 5

#print ( cadena + numerico)

#Bloques try-except separados para distintos casos
try: 
    print (numerador / denominador)
    
except ZeroDivisionError:
    print ("Ha ocurrido una división por cero")

try: 
    
    print (cadena + numerico)
except TypeError: 
    print ("Ha ocurrido una concatenación errónea")


#Bloque try--varios Excepts

try:
    print(10/0)
except TypeError:
    print("Ha ocurrrido un error de tipo")
except:
    print ("Ha ocurrrido un error desconocido")

print ("Fin del programa")

#Validacion en un ciclo infinito de peticion de datos

while True:
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        print("El resultado es: ", dividendo/divisor)
        break
    except ValueError:
        print("Debe ingresarse un número")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

print("fin del programa")

