#Uso de la sentencia continue
# for numero in range(1, 11):                # for con continue
#     if numero % 2 == 1:
#         continue
#     else :
#         print(f"{numero} es un numero par")


# numero =0
# while numero < 11:
#     if numero % 2 == 0:
#         continue
#     print(f"{numero} es un numero impar")

################################################################
#Uso de la sentencia break

# numero = int (input("Ingrese un digito"))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos +=1

#     if numero == buscado:
#         print(f"el numero {numero} fue encontrado en {intentos} intentos" )
#         break
#     elif numero < buscado :
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2 

# print("Fin del programa")

####################################################################
# Ejemplo de la funcion exit ()

# numero = int (input("Ingrese un digito"))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos +=1

#     if numero == buscado:
#         print(f"el numero {numero} fue encontrado en {intentos} intentos" )
#         exit()
#     elif numero < buscado :
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2 

# print("Fin del programa")


###########################################
# Programa de listas

lista = []

alumnos = 0
while alumnos <= 5:
    opcion = input("Agregar alumno (1) o terminar (2)")
    if opcion == "1" :
        nombre = input ("Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificación de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
        alumno = [nombre, calificacion1, calificacion2]
        lista.append(alumno)
        alumnos +=1
    elif opcion == "2":
        print(f"El programa ha terminado con {alumnos} alumnos")
        break
    else:
        print("Se ha ingresado una opcion inválida")
        continue

print("La lista de alumnos es: ")
print(lista)