
#LISTA PRODUCTOS

#INICIO DE LA FUNCION
def productos(listado,producto,precio):
    print("+-------------------------------------+")
    print("|Seleccione  |Producto       |Precio  |")
    print("+-------------------------------------+")
    for x in range(10):
        print("   "+str(listado[x])+ "          "+str(producto[x])+"         "+str(precio[x])+"     ") 
    print("+-------------------------------------+")    
               
        
        