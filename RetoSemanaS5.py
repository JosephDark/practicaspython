primerA = input ("Introduce al año actual:")
segundoA =input("Introduce el otro año para calcular: ")

if primerA.isnumeric() and segundoA.isnumeric():

    year1 = int(primerA)
    year2 = int(segundoA)

    if year1 == year2:
        print ("Has introducido el mismo año que el actual")
    elif year1 < year2: 
        resultado = year2 - year1

        if resultado <= 1:
            print(f"Para llegar a {year2} hace falta un año")
        else:
            print(f"Faltan {resultado} años desde {year1} hasta {year2}")

    elif year1 > year2: 
        resultado = year1 - year2

        if resultado <= 1:
            print(f"Desde {year2} ha pasado un año")
        else:    
            print(f"Han pasado {resultado} años desde {year2} hasta {year1}")
