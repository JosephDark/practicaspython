#Ejemplos de la funcion Print
print("Hola mundo")
print("Hola mundo", "Otra vez")
print("Son las", 9,"de la mañana")
print("El resultado de 3 * 4 es:", 3*4)

#Ejemplos con cadenas formateadas
print ("El numero 15 es sistema decimal es %d, en sistema octal es %o, en sistemas hexadecimal es %x" % (15,15,15))

pi = 3.141592
r = 5
print(f"El radio de un circulo es {r} y el area de ese circulo {pi * r ** 2: .2f}")

#Impresion de caracteres especiales
print("la letra beta es: \n\t \u03B2")

#Impresion de caracteres de escape
print("Hola mundo", end =" ") #Final de linea espacio ne blanco
print("otra vez", end = " \t")#Final de linea tabulador
print("y otra vez")#final de linea salto de linea
