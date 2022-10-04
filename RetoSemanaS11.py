
import m_retosemanal as cad
lista_fake= [["armando","iris","fay"],["martha","michelle"],["patito","danny","erick","miguel"]]
lista_principal=[]
sub_lista=[]
no_listas = cad.num_listas()
print(no_listas)

for i in range(no_listas) :
    tamano_lista = cad.verificar_numero()
    cad.crea_lista(sub_lista,tamano_lista)
    lista_principal.append(sub_lista)
    sub_lista = []

#print(lista_principal, end="\n \n")

print("Listas originales")
for i in range(no_listas):
    print(f"{i+1}.- {lista_principal[i]}")
#print(lista_fake)

#cad_a_eliminar = input("Escoje el numero de cadena que quieras eliminar sus elementos de las demas cadenas:")

while True:#cad_a_eliminar.isalpha(): #and not cad_a_eliminar in range(no_listas):
    
    try:
        cad_a_eliminar = int(input("Escoje el numero de cadena que quieras eliminar sus elementos coincidentes de las demas cadenas: "))
        if not cad_a_eliminar in range(no_listas+1):
    
            print("No es un numero de cadena valido.", end="\n \n")
        else:
            break
        #break
    except:
        print("No es un numero de cadena valido.", end="\n \n")

print(f"Escogiste un numero de cadena valido: {cad_a_eliminar}")
cad_a_eliminar-=1

for i in range (no_listas):
    if i == (cad_a_eliminar):
        continue
    else:
        cad.eliminacion(lista_principal[i],lista_principal[cad_a_eliminar])

print("Listas despues de la eliminacion")
for i in range(no_listas):
    print(f"{i+1}.- {lista_principal[i]}")
