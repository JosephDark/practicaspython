
lista = []


alumnos = 0

cantidad_alumnos = input ("¿Cuantos alumnos deseas ingresar?: ")

#qty_alumnos = int(cantidad_alumnos)


while not cantidad_alumnos.isdigit() or int(cantidad_alumnos) >=10 or cantidad_alumnos.isalpha():
    print("Opcion  inválida", end = "\n")
    cantidad_alumnos = input ("¿Cuantos alumnos deseas ingresar?: ")
    #qty_alumnos = int(cantidad_alumnos)



while alumnos < int(cantidad_alumnos):
    opcion = input("Agregar alumno (1) o terminar (2) ")
    if opcion == "1" :
        nombre = input ("Ingrese el nombre del alumno: ").capitalize()
        boleta = []
        boleta.append(nombre)
        cont_calif = 1

        

        for i in range(3):
            calificacion = int(input(f"Ingrese la calificación de {nombre}: "))
            boleta.append(calificacion)

            if cont_calif <3: 
                opcion2 = input(f"¿Desea ingresar otra calificacion de {nombre}?: (1) Si (2) No: ")

                while opcion2 != "1" and opcion2 != "2":
                    print("se ha tecleado una opcion invalida")
                    opcion2 = input(f"¿Desea ingresar otra calificacion de {nombre}?: (1) Si (2) No: ")


                if opcion2 == "1":
                    #boleta.append(calificacion)
                    cont_calif +=1
                elif opcion2 == "2":
                    #boleta.append(calificacion)
                    break
                # else:
                #     print("se ha tecleado una opcion invalida")
                #     continue
                #     #opcion2 = input(f"¿Desea ingresar otra calificacion de {nombre}?: (1) Si (2) No: ")

        lista.append(boleta)            
        # calificacion1 = int(input(f"Ingrese la primera calificación de {nombre}: "))
        # calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
        # alumno = [nombre, calificacion1, calificacion2]
        # lista.append(alumno)
        alumnos +=1
    elif opcion == "2":
        print(f"El programa ha sido terminado con {alumnos} alumnos")
        break
    else:
        print("Se ha ingresado una opcion inválida")
        continue

print(f"El programa ha terminado con {alumnos} alumnos")
print("La lista de alumnos es: ", end = "\n")



for x in range(len(lista)):
    print(lista[x], end = "\t")
    suma = 0
    contador = 0
    for i in range(len(lista[x])):
        if i == 0:
            continue
        else:
            suma = suma + int(lista[x][i])
            contador = contador + 1

    promedio = suma / contador  
    print(f"Promedio: {promedio}", end = "\n")      


#print(lista)