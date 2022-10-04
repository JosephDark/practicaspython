def verificar (letra):
    valor = ord(letra)

    if valor == 65 or valor == 97:
        anterior = valor + 25
        print(chr(anterior))
    else:
        print(chr(valor - 1))


    print(chr(valor))

    if valor == 90 or valor == 122:
        siguiente = valor - 25
        print(chr(siguiente))
    else:
        print(chr(valor + 1))

    
 



while True:
     
    print("Estas en un programa de bucle infinito. Solo podrás salir de él si ingresas la letra i")
    letra = input ("¿Qué letra deseas ingresar:")

    while not letra.isalpha() or len(letra)>1:
        print("Esa no es una letra.")
        letra = input ("¿Qué letra deseas ingresar:")
   
    if letra == "i" or letra =="I":
        print("Adios, has salido del ciclo")
        verificar(letra)
        break
    else:
        print("Me parece que quieres seguir un rato por aqui")
        verificar(letra)

    




