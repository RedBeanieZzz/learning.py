import random
list_=[]
list_alum=[]

def seleccion(nms):
    for i in range(len(nms)) :
        mayor=i
        for j in range(i+1, len(nms)) :
            if nms[j] > nms[mayor] :
                mayor= j
        nms[i], nms[mayor]= nms[mayor], nms[i]

def alum_not(name, nota1, nota2, nota3):
    list_alum.append(name)
    list_alum.append(nota1)
    list_alum.append(nota2)
    list_alum.append(nota3)

def prom_alum (nota1, nota2, nota3, name) :
    prom_=(nota1+ nota2+ nota3)/3
    list_.append((prom_, name))

#Fibonacci

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return b 
for x in range(10):
    print (fibonacci(x))

#Funcion de carga de matriz,
#establecer "data" con las variables necesarias
#f o c y range pueden variar
mi_matriz=[]
def matriz_carga(data):
    f=0
    c=0
    x=0
    for f in range(x):
        mi_matriz.append([])
        for c in range(x):
            mi_matriz[f].append([data])


#ordenamiento por insercion
def ord_insercion(lista):
 
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
        print (("DEBUG: "), lista)
 
def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j-1]:
        lista[j] = lista[j-1]
        j -= 1
    lista[j] = v

#calculo_edad
def calculoedad(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365)
    print(" tu edad es ", age, " años. ")