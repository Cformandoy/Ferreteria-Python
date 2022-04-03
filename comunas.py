
#LISTA COMUNAS

def comunasPrint(listado,comunas,comunaPrecio):
    print("+------------------------------------+")
    print("|Seleccione  |Comunas       |Precio  |")
    print("+------------------------------------+")
    
    for x in range(5):
        print("| "+str(listado[x])+"            "+str(comunas[x])+"        "+str(comunaPrecio[x])+"   |")
    print("+------------------------------------+")