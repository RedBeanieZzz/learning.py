#una fabrica de muebles hace butacas mesas y SIllas,
#esas con 3 modelos, eco, medio, luxury
#butacas: cada mes hacen 20 modelos de eco, 15 de medio, y 10 luxury
#mesas: 12 eco, 8 medio, 5 lux
#sillas: 18eco, 20med, 12lux
#representar la info en una matriz y calcular la prod de un año


fabrica=[[20,15,10],
        [12,8,5],
        [18,20,12]
]

def multipl_(empresa):
        for j in range(len(empresa)):
                for i in range(len(empresa)):
                        empresa[j][i]*=12
        return empresa
multipl_(fabrica)

print("\nLa produccion anual es: \n")
print("\tBasic/ Mid /Luxury", "\n", "-"*20)
print("Butacas: "+ str(fabrica[0]),"\n", "-"*20)
print("Mesas:   "+ str(fabrica[1]),"\n", "-"*20)
print("Sillas:  "+ str(fabrica[2]), "\n")