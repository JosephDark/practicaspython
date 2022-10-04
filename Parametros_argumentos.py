def sumar (parametro1, parametro2):
    """funcion que suma dos paramatros y los muestra en pantalla"""
    print("suma", parametro1 + parametro2)

argumento1 = 5
argumento2 = 7

#invocando a la funcion por medio de variables
sumar(argumento1,argumento2)

#invocando a la funcion por medio de parameteos de valor
sumar("mundo", "Hola")
#Los argumentos son posicionales, debemos colocarlos en el orden que pida la funcion
sumar("Hola ", "mundo")

def muestra_alumno(nombre, edad = 18, sexo = "F"):
    """Funcion que muestra en pantalla el nombre, edad y sexo de un alumno
    1.-Nombre
    2.-Edad
    3.-Sexo"""
    print(f"Nombre: {nombre}, Edad {edad}, Sexo {sexo}")

#Si en en parametro no especificamos un valor, es OBLIGATORIO. Si no especificamos, es OPCIONAL
#Ejecucion con parametro obligatorio
muestra_alumno("maria")

#Ejecucion con parametro obligatorio y uno opcional
muestra_alumno("maria", 22)

#Ejecucion con parametro obligatorio y el ulltimo
muestra_alumno("Juan", sexo="M")