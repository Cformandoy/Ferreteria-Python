#   Sistema para Ferreteria - Tienda Productos
#   
#   ESTUDIANTE : CRISTOPHER ADRIAN POZAS FORMANDOY
#   
#   DOCENTE    : SEGUNDO GALDAMES
#   SECCION    : ISI504 - 3600 AUTOMATIZACION - AIEP - BELLAVISTA  
#   FECHA      : SABADO 02 DE ABRIL 2022
# 
# #IMPORTACION DE LIBRERIAS Y FUNCIONES
from email.policy import strict
import os                   #Libreria para Borrar Consola
import time                 #Libreria para pausar el tiempo
from turtle import clear    #Libreria para Borrar Consola
from clear import *         #FUNCION borrarConsola
from introduccion import *  #FUNCION introduccion
from productos import *     #FUNCION productos
from carritoCompras import *#FUNCION carritoCompras
from comunas import *       #FUNCION comunas
from despacho import *      #FUNCION despacho
from addProductos import *  #FUNCION addProductos
from totalPagar import *    #FUNCION totalPagar

#-----------------------------------------------------------------------

#LISTAS

#PRODUCTOS Y PRECIOS
listado = [1         , 2         ,3          , 4         , 5         , 6         , 7         , 8         , 9         , 10]
producto=["Producto1","Producto2","Producto3","Producto4","Producto5","Producto6","Producto7","Producto8","Producto9","Producto10"] #PRODUCTOS DISPONIBLES
precio= [1500        , 1200      ,3500       , 800       , 4300      , 1400      , 5000      , 4800      , 15000     , 12500]       #PRECIO DE LOS PRODUCTOS

#COMUNAS Y PRECIOS
comunas=["comuna1","comuna2","comuna3","comuna4","comuna5"] #COMUNAS PARA DESPACHO
comunaPrecio=[1000,2000     ,2500     ,2800     ,3000]      #PRECIO DEL DESPACHO A COMUNAS


#-----------------------------------------------------------------------

#CODIGO PRINCIPAL
clearConsole()                                                  #BORRADO DE CONSOLA
introduccion()                                                  #FUNCION DE INTRODUCCION-BIENVENIDA
time.sleep(5)                                                   #TIEMPO PARA LECTURA
clearConsole()                                                  #BORRADO DE CONSOLA
productos(listado, producto, precio)                            #SE MUESTRA LA TABLA-LISTA PRODUCTOS
k,total, carritoProducto, carritoPrecioProducto = addProductos (listado, producto, precio) #AGREGACION DE PRODUCTOS
clearConsole()                                                  #BORRADO DE CONSOLA
carritoCompras(k,carritoProducto,carritoPrecioProducto,total)   #IMPRIME EL CARRITO DE COMPRAS Y TOTAL
precioDespacho = despacho(listado,comunas,comunaPrecio)         #CONSULTA DE DESPACHO, SELECCION DE COMUNA Y CALCULO DEL PRECIO
carritoCompras(k,carritoProducto,carritoPrecioProducto,total)   #IMPRIME EL CARRITO DE COMPRAS Y TOTAL
totalPagar(total, precioDespacho)                               #IMPRIME EL COSTO DESPACHO Y TOTAL A PAGAR

