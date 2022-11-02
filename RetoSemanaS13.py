from re import L

lista_alumnos=[]

while True:
    while True:
        print("### MENU ####")
        print("— Agregar un nuevo alumno (1)")
        print("— Ver los alumnos y las calificaciones (2)")
        print("— Salir (S)")
        opcion = input("Elija la opción deseada: ")

        if opcion == "1":  #### INGRESO DE UN ALUMNO ####
            #Ciclo de Validacion del nombre
            while True:   
                boleta = [] 
                nombre = input("Ingrese su nombre: ").capitalize()
                appaterno = input ("Ingrese su apellido paterno: ").capitalize()
                apmaterno = input ("Ingrese su apellido materno: ").capitalize()
                #print("Agregar un nuevo alumno") #Print de control
                if nombre == "" or appaterno == "" or apmaterno == "":
                    print("No has escrito nada en uno o más campos del nombre")
                else:
                    break
            #Ciclo de validacion del numero de calificaciones a ingresar
            while True:
                try:
                    numcalif= int(input("¿Cuantas calificaciones desea ingresar?"))
                    if numcalif == 0:
                        print("No es un numero válido")
                    else:
                        break
                except:
                    print("No es un numero válido")

            #Metemos el nombre a la boleta
            boleta.append(nombre +" "+ appaterno+" "+ apmaterno)
            #Pedimos las calificaciones
            for i in range(numcalif):
                while True:
                    try:
                        calif = int(input("Ingrese la calificacion: "))
                        if calif > 10 or calif < 0:
                            print("Valor erróneo para la calificación")
                        else:
                            boleta.append(calif)
                            break
                    except ValueError:
                        print("Valor erróneo para la calificacion")

            #Ingresamos la boleta a la lista de alumnos
            lista_alumnos.append(boleta)
            #print(lista_alumnos)



        


            break
        if opcion == "2": #### MOSTRAR A LOS ALUMNOS ####
            #Verificamos que la lista no esté vacía
            if lista_alumnos == []:
                print("La lista esta vacia.", end = "\n \n")
            else: #Si no esta vacía, calculamos promedio e imprimimos
                print("### Ver las Calificaciones de los alumnos ###", end = "\n")
                numAlumnos = len(lista_alumnos) #Sacamos el numero de alumnos
                temp1=[] #creamos lista temporal para el nombre del alumno (creo que esto sobraba al final)
                temp2=[] #creamos lista temporal para las operaciones con las calificaciones del alumno

                for i in range(numAlumnos):
                    temp1 = lista_alumnos[i][0]#sacamos el nombre del alumno
                    temp2 = list(lista_alumnos[i]) #copiamos la boleta del alumno
                    temp2.pop(0)#removemos el nombre del alumno para calcular el promedio
                    promedio = sum(temp2)/len(temp2)
                    print ("Alumno: ", temp1)
                    print ("Calificaciones: ", temp2)
                    print("Promedio: ", promedio)

                #print(lista_alumnos) #print de control
            break
        if opcion == "S": ### SALIDA DEL PROGRAMA ###
            
            while True: #Ciclo de cerrado del programa
                confirmacion = input("Se cerrará el programa. ¿esta seguro? (S)")
                if confirmacion== "S":
                    exit()
                else:
                    print("No has ingresado una opcion válida.")
        else:
            print("Opción inválida", end = "\n \n")
            
        


            

        


        
            
           

