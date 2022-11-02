personas =[]

def captura_alumno():
    contacto2=[]  #Lista temporal para integrar los datos del contacto
    while True:
        while True:  #Ciclo de revision del nombre completo  
            nombre = input("Introduce tu nombre: ").capitalize()
            appaterno = input ("Introduce tu apellido paterno: ").capitalize()
            apmaterno = input ("Introduce tu apellido materno: ").capitalize()
            if nombre == "" :
                print("No introduciste tu nombre")
            elif appaterno == "":
                print("No has introducido tu apellido paterno")
            elif apmaterno == "":
                print("No has introducido tu apellido materno")
            else:
                contacto2.append(nombre)    #Añadimos nombre al registro
                contacto2.append(appaterno)
                contacto2.append(apmaterno)
                break

        while True:#Ciclo para introducir y validar edad
            try:
                edad = int(input("Introduce tu edad: "))
                if edad < 0 or edad >= 100: #Rango de edad entre 1 y 99
                    print("Edad inválida")
                else:
                    contacto2.append(edad)  #Añadimos edad al registro
                    break
            except ValueError:
                print("Valor inválido para la edad")


        correo = input("Introduce tu correo: ")
        contacto2.append(correo)  #Añadimos correo al registro
       

        while True: #Ciclo de revision del telefono
            try:
                telefono = input("Introduce tu telefono: ")
                int(telefono) #Verificamos que sea un numero
                contacto2.append(telefono) #Ingresamos el telefono a la lista
                break
            except ValueError:
                print("Valor inválido para telefono")

        #personas.append(contacto)
        return contacto2 #Regresamos la lista completa a la variable asignada en el cuerpo del programa

while True:    

    print("""
    1.- Agregar personas a la agenda.
    2.- Guardar persona en la agenda.
    3.- Imprimir en pantalla la agenda.
    4.- Modificar contacto de la agenda.
    5.-Salir.
    """)

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        contacto = []
        contacto = captura_alumno()

        

        personas.append(contacto)
        #contacto = []
    elif opcion == "2":
        with open("agenda.txt","a") as f_agenda:
            #for persona in personas:
            #    f_agenda.write(f"{persona[0]} {persona[1]} {persona[2]} Edad:{persona[3]} Correo: {persona[4]} Telefono: {persona[5]} \n")
            f_agenda.write(f"{contacto[0]} {contacto[1]} {contacto[2]} Edad:{contacto[3]} Correo: {contacto[4]} Telefono: {contacto[5]} \n")
        print("Datos guardados en la agenda")
    elif opcion == "3": #Mostrar los contactos almacenados
        with open("agenda.txt","r") as f_agenda:#Abrimos archivos
            numero_de_lineas = 0 #Inicializamos contador de líneas
            for i in f_agenda:
                
                numero_de_lineas+=1
                print(f"Linea {numero_de_lineas} : {i}") #imprimimos linea

            print(f"El archivo tiene {numero_de_lineas} contactos.")
    elif opcion == "4":
        #Mostrar lista de la agenda para ver qué contacto quieres modificar
        with open("agenda.txt","r") as f_agenda:
            numero_de_lineas = 0
            for i in f_agenda:
                
                numero_de_lineas+=1
                print(f"Linea {numero_de_lineas} : {i}") #Impresion de contacto
        
        while True:  #Ciclo para modificar el registro
            try:

                numeroAgenda= int(input("¿Que numero de contacto desea modificar?: "))
                if numeroAgenda <= 0 or numeroAgenda > numero_de_lineas:
                    print("Numero de contacto no válido")
                else:
                    numeroAgenda-=1 #Restamos 1 al numero de linea para ubicar el resgistro
                    with open("agenda.txt","r") as f_agenda: #Abrimos en modo lectura
                        lista_agenda = f_agenda.readlines() #Sacamos el archivo a una variable
                        
                        contacto = captura_alumno() #capturamos los nuevos datos
                        
                        #print(contacto) #print de control
                        #Creamos la cadena del registro a modificar
                        cadena = f"{contacto[0]} {contacto[1]} {contacto[2]} Edad:{contacto[3]} Correo: {contacto[4]} Telefono: {contacto[5]} \n"
                        lista_agenda.pop(numeroAgenda) #Quitamos el registro anterior
                        lista_agenda.insert(numeroAgenda,cadena)#insertamos el nuevo registro
                        #print(lista_agenda[numeroAgenda]) #print de control

                    with open("agenda.txt","w") as f_agenda: #Abrimos en modo escritura completa
                        f_agenda.writelines(lista_agenda)#Rescribimos todo el archivo.
                        print("Registro modificado")
                    break
            except ValueError:
                print("Valor inválido")
    elif opcion =="5":
        print("Salir del programa")
        exit()
    else:
        print("opcion inválida")





