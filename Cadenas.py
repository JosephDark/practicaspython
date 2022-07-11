Texto_variado = "Palabra 123"
print(type(Texto_variado))

#Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print("""
# Funcionamiento de \
# programa:(opciones)
#         -1 para acceder a opciones
#                 -2 para salir """)
###########################################################################

#Suscripting e indexado
# texto = "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) #Marca error porque la cadena va de 0 a 5
# print(texto[-7]) #Error, no podemos acceder a una posición que no existe

# letra = texto[0] #Asignamos un indice de la cadena a una variable de texto
# print (letra)

# #texto[0] = "p" #Error, no podemos modificar un indice especifico de una cadena 

# texto_compuesto = letra + texto[1] #concatenacion
# print(texto_compuesto)

#################################################

#Slicing o substringing

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])

################################################
#Cadenas y formatos
# Texto = "Hola mundo buenas tardes"
# print(Texto.lower())
# print(Texto.upper())
# print(Texto.capitalize())
# print(Texto.title())
# print(Texto.swapcase())

#texto = texto.upper()  #se reasinga el valor de texto, ahora en mayusculas
#print(texto) 

print("{} + {} = {}".format(2,3,2+3))
print("{} + {} = {}".format("Hola","Mundo","Hola Mundo"))
print("{:.3f} + {:.4f} = {}".format(2,3,2+3))
print("{1} + {0} = {2}".format(2,3,2+3))
print("{2} + {0} = {1}".format("Hola","Mundo", "Hola Mundo"))
print("{:d} = {:b} = {:o} = {:x}".format(15,15,15,15))
