# f_archivo = open ("archivo1.txt","w") #Creacion/Apertura de archivo
# print(f_archivo) #Impresion de las caracteristicas del archivo
# f_archivo.write("Hola Mundo!") #Escribimos dentro del archivo
# f_archivo.close() #Cerramos el archivo

# f_archivo = open ("archivo1.txt","w") #Abrimos
# f_archivo.write("Este es mi primer archivo") #Sobreescribimos el contenido del archivo
# f_archivo.close()#Cerramos el archivo

# f_lectura = open("archivo1.txt", "r") #Abrimos en modo lectura
# print(f_lectura.read()) #Leemos el contenido del archivo
# f_lectura.close() #Cerramos el archivo

# print(f_archivo)#Imprimos las características del archivo.
# print(f_lectura)

################################################################################
#Manejo de archivos con With y As

f_lectura= open ("archivo1.txt","r") #Abrimos en modo lectura
print(f_lectura.closed)#Checamos si esta cerrado. No esta cerrado por lo tanto imprime 'False'
f_lectura.close()#Cerramos el archivo
print(f_lectura.closed)#Checamos si esta cerrado el archivo. Esta cerrado por lo tanto imprime 'True'

with open("archivo1.txt","r") as f_lectura: #Abrimos el archivo con el nombre de objeto f_lectura 
    print(f_lectura.closed) #Verificamos si esta cerrado. Esta abierto por lo tanto imprime 'False'
                            #El archivo permanecera abierto mientras estemos en el cuerpo del With
                            #y se cerrará automáticamente al salir de él
print(f_lectura.closed)#Verificamos si esta cerrado. Esta cerrado por lo tanto imprime 'True'

########################################################################################
#Escribir al final del archivo (mooo append 'a')
with open("archivo1.txt","a") as f_archivo: #Abrimos el archivo con el nombre de objeto f_lectura modo append
   f_archivo.write("\nEste es mi primer archivo 2")#Inserte salto línea y texto
   f_archivo.write("Este es mi primer archivo 3")# Inserta texto
   f_archivo.write("\n")#Inserta salto de línea
   f_archivo.write("\t Este es mi primer archivo 4") #Inserta tabulacion y texto

with open("archivo1.txt","r") as f_lectura:
    print(f_lectura.read())#Imprime contenido del archivo.

#########################################################################################
#Asignar contenido de un archivo a una variable 

with open("archivo1.txt","r") as f_lectura:
    contenido = f_lectura.read()    #sacamos contenido, lo mandamos a contenido
    print(f"****{contenido}*****")#see imprime y se queda el cursor en el EOF
    contenido = f_lectura.read() #Sacamos contenido, pero al estar al EOF,
    print(f"****{contenido}*****")#imprime puro vacio

#########################################################################################
#Leer archivo linea por línea
with open("archivo1.txt","r") as f_lectura:
    numero_de_lineas = 0 #Contador de lineas 
    for i in f_lectura: #cada i es una linea del archivo
        numero_de_lineas +=1 #Incrementamos contador
        print(f"Linea {numero_de_lineas} : {i}") #Imprimimos linea extraída
    print (f"El archivo tiene {numero_de_lineas} lineas")
