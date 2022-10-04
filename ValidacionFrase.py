


frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")

while not frase.isalpha() :    #Validamos mediante isalpha solo tengamos letras en la cadena
    print("La frase solo debe contener letras. Intente de nuevo")  #Y el ciclo se repite mientas no
    frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ") #se cumpla esta condicion


flag = "1"    #Flag es una bandera que controla el ciclo de revision de la cadena escrita

while flag == "1":
    if len(frase) < 4 :    #Caso 1 la frase tiene menos de 4 letras
        print(f"Hacen falta letras. Sólo tiene {len(frase)} letras.")
    
    
    elif len(frase) == 1:   #Subcaso del caso uno: solo hay una letra en la frase
        print(f"Hacen falta letras. Sólo tiene {len(frase)} letra.")
    elif len(frase) > 8 :   #Caso 2 la frase tiene mas de 8 letras.
        print(f"Sobran letras. Tiene {len(frase)} letras")
    
                            #caso 3 la frase tiene entre 4 y 8 letras
    elif len(frase)>=4 and len(frase)<=8 :
        print(f"La frase es {frase}. La frase es correcta")
    
    flag = input("¿Desea comprobar otra frase? (1) Si (2) No.")  #LA bandera controla la repeticion

    if flag == "1":

        frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")
        while not frase.isalpha() :
            print("La frase solo debe contener letras. Intente de nuevo")
            frase = input("Ingresa una frase con mínimo 4 letras y máximo 8: ")
    elif flag== "2":
        print("Eligio terminar el programa")
        exit()
    else:
        print("Opcion invalida. Se cerrará el programa")
        exit()

    




