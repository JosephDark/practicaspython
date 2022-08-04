contrasena = input("Ingrese una contraseña: ")

while contrasena[0].isalpha():
    print("La contraseña debe de comenzar con un numero.")
    contrasena = input("Ingrese una contraseña: ")



for i in range(2):

    contrasena2 = input("Ingrese la contraseña nuevamente: ")
    if contrasena == contrasena2 :
        print("Contraseña correcta. ", end ="\n")
        break
    else:
        print("Las contraseñas no coinciden.")
        
 
print("Fin del programa.")