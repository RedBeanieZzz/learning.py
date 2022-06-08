#mostrar_estrellas

show_stars=5
def list(nms):
    n=0
    while n < nms :
        n+=1
        print("*"*n)
    return n
list(show_stars)

lista_total=[1,2,3,4,5,6,7,8,9,10]
print("-"*30)
def listapar(list):
    par_=[]
    for n in range(len(list)):
        if n%2==0 :
            par_.append(n)
    print(par_)
    return n

listapar(lista_total)
'''#listas[]se puede modificar
lista=[1,2,3,4]
#tuplas()no se puede modificar
tupla=("caos",12,3.14,True)
print(type(tupla))

#diccionarios{} con llaves!(clave:valor)
cliente={"nombre": "Julian", "edad": 18, 200: True}

print(cliente["nombre"])
cliente["edad"]= 20
#agregar elemento
cliente["Direccion"] = "Jose luis perales 335"
#eliminar elemento
del cliente[200]
print(cliente)

for d in cliente:
    print(cliente[d])
'''
