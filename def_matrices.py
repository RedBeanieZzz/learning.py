matriz=[[2,4],[4,6]]
matriz1=[[],[]]
resultado=[[0,0],[0,0]]
mi_matriz=[]
#matriz basica
def matriz_carga(data):
    f=0
    c=0
    x=3
    for f in range(x):
        mi_matriz.append([])
        for c in range(x):
            mi_matriz[f].append([data])
data=20
matriz_carga(data)
print(mi_matriz)

def suma_matriz(A,B):
    for i in range(len(A)):
        for j in range(len(A)):
            resultado[i][j]=matriz[i][j]+matriz1[i][j]

def mult_matriz(A,B):
    for i in range(len(A)):
        for j in range(len(A)):
            resultado[i][j]=matriz[i][j]*matriz1[j][i]

def trasp_matriz(A):
    for i in range(len(A)):
        for j in range(len(A)):
            resultado[i][j]=matriz1[j][i]

def opuesta_matriz(A):
    for i in range(len(A)):
        for j in range(len(A)):
            resultado[i][j]=matriz1[j][i]*-1

def cadena_matriz(A):
    cadena = ""
    for i in range(len(A)):
        cadena += "["
        for j in range(len(A[i])):
            cadena +="{:>4s}".format(str(A[i][j]))
        cadena +="   ]\n"
    return cadena    

for i in range(2):
    filas=int(input("Ing los elementos para las filas: "))
    matriz1[0].append(filas)

for j in range(2):
    columnas=int(input("ing los elementos para las columnas: "))
    matriz1[1].append(columnas)

#en estas lineas paso los parametros a la función e imprimo el resultad de la suma   

suma_matriz(matriz, matriz1)
cadmatriz=cadena_matriz(resultado)
print("el resultado de la suma de las dos matrices es: ")
print(cadmatriz)

#paso paramtrs a función y mult las matrices

mult_matriz(matriz, matriz1)
cadmatriz=cadena_matriz(resultado)
print("el resultado de la multiplicación de las dos matrices es: ")
print(cadmatriz)

#imprimo la matriz traspuesta

trasp_matriz(matriz1)
cadmatriz=cadena_matriz(resultado)
print("el resultado de la trasp de las dos matrices es: ")
print(cadmatriz)

#imprimo la matriz opuesta

opuesta_matriz(matriz1)
cadmatriz=cadena_matriz(resultado)
print("la matriz opuesta es: ")
print(cadmatriz) 