#Probandoambitos
titulo = "Probando ámbitos"
suma = 10.5

def sumar():
    suma = 2 + 2
    #titulo = titulo + "mundo"
    #print(titulo)
    print("suma en ambito local",suma, id(suma))

print("Antes de llamar a la funcion")
print("suma en ambito global",suma, id(suma))
sumar()
print("Despues de llamar a la funcion")
print("suma en ambito local",suma, id(suma))
