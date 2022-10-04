import matplotlib.pyplot as plt

def grafica_ventas(notas, color, titulo):
    """
    Diibujar una grafica con las ventas por año
    """

    plt.plot(notas.keys(), notas.values(), color = color)
    plt.title(titulo)
    plt.show()


while True:
    primer_year= input("¿Cual es el primer año del periodo?")
    
    try:
        if int(primer_year) >= 1900 and int(primer_year)<= 2030:
            break
        else:
            print("Año inválido")
    except:
        print("Año inválido")

while True:
    segundo_year= input("¿Cual es el segundo año del periodo?")
    
    try:
        if int(segundo_year) >= 1900 and int(segundo_year)<= 2030:
            break
        else:
            print("Año inválido")
    except:
        print("Año inválido")

print(f"El periodo va desde {primer_year} hasta {segundo_year}.", end= "\n \n")

lista_años = []
lista_ventas=[]

limite1 = int(primer_year)
limite2 = int(segundo_year)
contador=limite1

#Este ciclo genera los años entre los dos años dados, lo guarda en un lista, pregunta las venta de ese año
#y lo guarda en otra lista, hasta completar los pares de año - venta
for i in range(limite1, limite2+1):
    
    #contador+=1
    lista_años.append(str(contador))
    while True:
        try:
            ventas=int(input(f"Ingrese las ventas del año {contador}: "))
            if int(ventas): 
                lista_ventas.append(ventas)
                break
            else:
                print("valor invalido")
        except:
            print("Valor inválido")
    contador+=1 




print(lista_años)
print(lista_ventas)

titulo = "Ventas del " + primer_year + " al " + segundo_year #GENERO EL TITULO DEL GRAFICO
datos = dict(zip(lista_años,lista_ventas))  #UNE LAS DOS LISTAS Y LAS PASA A DICCIONARIO

print(datos) #IMPRIMO EL DICCIONARIO

grafica_ventas(datos,"blue",titulo) #MANDA EL DICCIONARIO A GRAFICAR, JUNTO 

