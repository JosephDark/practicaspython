#Utilizar al menos dos funciones
#Preguntar cuantos alumnos se registraran, en caso de no registrarse se asume que al menos son tres alumnos
#Preguntar el nombre y 2 calificaciones 
#Mostrar el nombre en pantalla con inicial mayuscula y al menos dos calificaciones
#Al final del programa se mostrara una lista con los alumnos y sus calificaciones 



def captura_alumnos(numero = 3):
    """registra alumnos y dos calificaciones
    Recibe como parametro la cantidad de alumnos a registrar
    Si no se especifica la cantidad de alumnos, se registraran 3
    """
    lista_alumnos =[]
    for i in range(numero):
        nombre = input(f"{i + 1}.- Ingrese el nombre del alumno:").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificacion de {nombre}:"))
        calificacion2 = int(input(f"Ingrese la primera calificacion de {nombre}:"))
        lista_alumnos.append([nombre,calificacion1,calificacion2])
        promedio(nombre,calificacion1,calificacion2)
    print("Las calificaciones de los alumnos son: ", lista_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    """
    
    Calcula el promedio de un alumno y los despliega en la pantalla por medio de un mensaje
    recibe como parametros el nombre y dos calificaciones del alumno
    """
    promedio= (calificacion1 + calificacion2) / 2
    print(f"El promedio de {nombre} es {promedio}")


numero_alumnos = input ("¿Cuantos alumnos desea registrar?")

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()
