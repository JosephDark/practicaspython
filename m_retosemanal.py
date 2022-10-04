# Modulo m_retosemanal(m_retosemanal.py)

""""Modulo que contiene las funciones de manejo de listas."""

def crea_lista(listas, valor=1):
    """
        Funcion que pregunta los nombres y los ingresa a una lista."""
    for i in range(valor):
        nombre= input ("¿Que nombre desea ingresar?: ")
        listas.append(nombre)


def eliminacion(listaA, listaB):
    """
        Esta funcion recibe dos listas, las compara y elimina los elementos iguales 
        en ambas listas en la primera lista
        """

    print(f"Las listas antes de la comparacion y eliminacion son {listaA} y {listaB}.")
    

    for i in listaB:
         for j in listaA:
             if j==i:
                 listaA.remove(j)

            
    
    print(f"Las listas despues de la comparacion y eliminacion son {listaA} y {listaB}.")

def verificar_numero():
    """
    Funcion que verifica que se ingrese un numero entero como tamaño de lista
    """
    while True:
        try:
            num = int(input("¿De que tamaño desea crear su lista?"))
            return num
        except:
            print("Ese no es un valor valido.")

def num_listas():
    """
    Funcion que verifica que se ingrese un numero entero como numero de listas
    """
    while True:
        try:
            num = int(input("¿Cuantas listas desea crear?"))
            return num
        except:
            print("Ese no es un valor valido.")