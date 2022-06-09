
'''
def buscador(oldarch, newarch):
    while 1:
        texto = oldarch.readline()
        if texto == "":
            break
        if texto[0] == "#":
            continue
        newarch.write(texto)
    oldarch.close()
    newarch.close()
    return

f1=open("filetest.py", "r")
f2=open("filetestnew.py", "w")

copia=buscador(f1,f2)
f2 = open ("filetestnew.py", "r")
print(f2.read())

f=open("newfile.py", "w")
x=54
f.write(str(x))
f.write("\n Linea1\n Linea2\n Linea3\n")
f.close()
f=open("newfile.py", "r")
print(f.readline())

f=open("newfile.py", "w")
autos=200
perro=5.5
ventas=("en el mes %s de junio vendimos %d autos " %(perro, autos))
f.write(ventas)
f=open("newfile.py", "r")
print(f.read())

f=open("newfiledata.py", "w")
print(f)
horas=23.5 
minutos=55
seg=54
kilo=20
cantidad=200
gramos=20

#formateo de frase
formato=("El dia tiene %s hs, %d min,
y %d seg\n El cajon tiene %d kilos, una
cant de %d y gramos %d  %(horas,minutos,seg,kilo,cantidad,gramos))
f.write(formato)
f.close()
f=open("newfiledata.py", "r")
A=(f.readlines())
print(A[0],A[1])
'''
#encurtido/deserializado
import pickle
f=open("newfiledata.py","wb")
pickle.dump([1,2,3], f)
pickle.dump(1.3, f)
f.close()
f=open("newfiledata.py", "rb")
z=pickle.load(f)
print(z)
x=pickle.load(f)
print(x)

