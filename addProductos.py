

#AGREGAR PRODUCTOS


#IMPORTACION DE LIBRERIAS
from clear import *
import time
from productos import *

#INICIO DE LA FUNCION
def addProductos(listado,producto, precio):
    carritoProducto = []
    carritoPrecioProducto = []

    agregar = "SI"
    k = 0
    total = 0

    while (agregar == "si" or (agregar == "SI") or (agregar == "Si")):
        
        #seleccion de usuario
        userSelect = input("Indique el producto que desea agregar al carrito: ")    #consulta
        userSelect = int(userSelect)
        if (userSelect >= 1) and (userSelect <= 10):                                #Verifica que el usuario seleccione un rango correcto
            carritoProducto.append(producto[(userSelect - 1)])                      #Busca en la tabla Producto y guarda en carritoProducto
            carritoPrecioProducto.append(precio[userSelect - 1])                    #Busca en la tabla Precio y guarda en carritoPrecioProducto
            k = k + 1                                                               #Conteo de productos agregados
            total = total + int(precio[(userSelect - 1)])                           #Calcula el precio de los productos agregados
            clearConsole()                                                          #borra consola
            print("+---------------------------+")
            print("|  PRODUCTO "+ str(userSelect) + " SELECCIONADO  |")             #Imprime el producto seleccionado
            print("+---------------------------+")
            time.sleep(1.5)                                                         #Pausa para lectura
            clearConsole()                                                          #borra pantalla
            productos(listado,producto,precio)                                      #funcion productos para mostrar la lista
            agregar = input("Desea agregar otro producto a su carrito? SI o NO: ")  #Consulta
        else:
            clearConsole()
            print("+-----------------------------------------------------+")
            print("|  PRODUCTO INGRESADO NO VALIDO, VUELVA A INTENTARLO  |")        #imprime un error
            print("+-----------------------------------------------------+")
            time.sleep(1.5)                                                         #pausa para letura
            clearConsole()                                                          #borra consola
            productos(listado,producto,precio)                                      #funcion productos para mostrar la lista
            agregar = "SI"                                                          #resetea la condicion
    return k,total, carritoProducto, carritoPrecioProducto
