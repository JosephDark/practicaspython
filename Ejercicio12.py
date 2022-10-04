import matplotlib.pyplot as plt

def diagrama_barras_calificaciones(notas, color, alumno):
    """
    Diibujar una grafica con las ventas
    """

    plt.bar(notas.keys(), notas.values(), color = color)
    plt.title("Calificaciones de " + alumno)




calificaciones = {
        "Programacion":3,
        "Español": 6.5,
        "Calculo": 4,
        "Historia": 8,
        "Biologia": 10

    }

alumno = input("Nombre del alumno: ")
diagrama_barras_calificaciones(calificaciones,"blue", alumno)
plt.show()