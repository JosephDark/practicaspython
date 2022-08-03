primerA = input ("Introduce al año actual:")
segundoA =input("Introduce el otro año para calcular: ")

if primerA.isnumeric() and segundoA.isnumeric(): #Validamos que ambas cadenas sean numeros 

    year1 = int(primerA)  
    year2 = int(segundoA)  

    if year1 == year2:   #Si el año actual es igual al año siguiente para calcular 
        print ("Has introducido el mismo año que el actual") 
    elif year1 < year2:             #Si el año actual es menor al año sigiente pedido, hay dos casos:  
        resultado = year2 - year1

        if resultado <= 1:      #Primer Caso la diferencia es igual o menor a 1 años              
            print(f"Para llegar a {year2} hace falta un año")
        else:                    #Segundo caso la diferecnia es mayor a 1, se calcula cuantos años faltan para Año 2
            print(f"Faltan {resultado} años desde {year1} hasta {year2}")

    elif year1 > year2:      #Si el año actual es mayor al año siguiente, hay dos casos
        resultado = year1 - year2

        if resultado <= 1:    #Primer Caso la diferencia es menor igual a uno,
            print(f"Desde {year2} ha pasado un año")
        else:                 #segundo caso, la difeencia es mayor a 1
            print(f"Han pasado {resultado} años desde {year2} hasta {year1}")
