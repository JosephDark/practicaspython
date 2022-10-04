diccionario_ingles={ "rojo":"red", "naranja":"orange", "amarillo":"yellow", \
    "verde":"green", "azul":"blue", "violeta":"violet"}

diccionario_aleman={ "rojo":"rot", "naranja":"orange", "amarillo":"gelb", \
    "verde":"grün", "azul":"blau", "violeta":"violett"}


flag = "1"

while flag == "1":

    idioma = input("""Escoja el idioma del dicionario
    1) Ingles
    2) Aleman 
    """)

    if idioma == "1":
        frase = input ("Escribe una frase:")
        frase = frase.lower()
        palabras = frase.split()
        respuesta =" "

        for palabra in palabras:
            if palabra in diccionario_ingles:
                respuesta = respuesta + diccionario_ingles[palabra] + " "
            else :
                respuesta = respuesta + palabra + " "

        print(respuesta)

    elif idioma == "2":
        frase = input ("Escribe una frase:")
        frase = frase.lower()
        palabras = frase.split()
        respuesta =" "

        for palabra in palabras:
            if palabra in diccionario_aleman:
                respuesta = respuesta + diccionario_aleman[palabra] + " "
            else :
                respuesta = respuesta + palabra + " "

        print(respuesta)
    else:
        print("opcion inválida")

    flag = input("¿Desea comprobar otra frase? (1) Si (2) No ")  #LA bandera controla la repeticion

    if flag == "1":
        continue
    elif flag== "2":
        print("Eligio terminar el programa")
        exit()
    else:
        print("Opcion invalida. Se cerrará el programa")
        exit()

