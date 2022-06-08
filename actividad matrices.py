
#lista de modelos, para cada modelo hay una matriz de 1x1, asi se evita mezcla de data

#variables de porcentaje rotas
mod_fail_1=2
mod_fail_2=5
mod_fail_3=8
mod_fail_4=10
#modelos fijos
modelo1=[[],[]]
modelo2=[[],[]]
modelo3=[[],[]]
modelo4=[[],[]]
#dañados y buenos totales
total_good=[[],[]]
total_fail=[[],[]]
result_good=([])
result_fail=([])
#------------------------
#funcion de carga de matrices de modelos, transp, y opac
def carga_matriz(matriz_modelo, fallas, total_fail, total_good):

    for f in range(1):
        transp_total=int(input("Ingrese la cantidad de bombillas TRANSPARENTES: "))
        matriz_modelo[0].append(transp_total)
        tr_fail=(transp_total*fallas)/100
        tr_good=transp_total-tr_fail
        total_fail[0].append(tr_fail)
        total_good[0].append(tr_good)
        for c in range(1):
            opacas=int(input("Ingrese la cantidad de bombillas OPACAS: "))
            matriz_modelo[1].append(opacas)
            op_fail=(opacas/100)*fallas
            op_good=opacas-op_fail
            total_fail[1].append(op_fail)
            total_good[1].append(op_good)
#----------------------
#llamar a la funcion, cargo modelo, %falla y matrices totales
carga_matriz(modelo1, mod_fail_1, total_fail, total_good)
carga_matriz(modelo2, mod_fail_2, total_fail, total_good)
carga_matriz(modelo3, mod_fail_3, total_fail, total_good)
carga_matriz(modelo4, mod_fail_4, total_fail, total_good)
#----------------------

#suma de datos totales por modelos,y resultado total final
result_good=(sum(total_good[0], sum(total_good[1])))
#total_good=([x[0] + x[1] + x[2] + x[3] for x in total_good])
#result_good=(sum(total_good))

result_fail=(sum(total_fail[0], sum(total_fail[1])))
#total_fail=([x[0] + x[1] + x[2] + x[3] for x in total_fail])
#result_fail=(sum(total_fail))
total_total=result_good+result_fail
#----------------------
#prints de prueba
print("-"*20)
print("Las bombillas transparentes y opacas del MODELO 1 son: ", modelo1 )
print("-"*20)
print("Las bombillas transparentes y opacas del MODELO 2 son: ", modelo2 )
print("-"*20)
print("Las bombillas transparentes y opacas del MODELO 3 son: ", modelo3 )
print("-"*20)
print("Las bombillas transparentes y opacas del MODELO 4 son: ", modelo4 )
print("-"*20)
#---------------------
print("La cantidad de bombillas buenas son: \n", total_good, "\n")
#---------------------
print("La cantidad de bombillas dañadas son: \n", total_fail, "\n")
print("-"*20)
#---------------------

print("El total de bombillas producidas es: ", total_total)
print("El total de bombillas buenas es: ", result_good)
print("\nEl total de bombillas falladas fue: ", result_fail)
print("-"*20)
