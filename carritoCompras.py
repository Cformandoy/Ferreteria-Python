
#CARRITO DE COMPRAS

#INICIO DE LA FUNCION 
def carritoCompras(k,carritoProducto,carritoPrecioProducto,total):
    print("+------------------------+")
    print("|   Carrito de compras   |")
    print("+------------------------+")
    print("| Producto     |Precio   |")
    print("+------------------------+")

    for x in range(k):
        print("| "+str(carritoProducto[x])+"      "+str(carritoPrecioProducto[x])+"    |") 
    print("+------------------------+")
    print("| TOTAL CARRITO    "+str(total)+"  |")
    print("+------------------------+")
    return total