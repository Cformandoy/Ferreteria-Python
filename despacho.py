
#DESPACHO DE CARRITO

#INICIALIZACION DE LIBRERIAS
from clear import *
from comunas import *
import time

#INICIO DE LA FUNCION
def despacho(listado, comunas, comunaPrecio):
    consultaDespacho= input("Desea despachar su carrito de compras? (SI O NO) : ")         #consulta
    condicion=0
    while condicion == 0:    
        if(consultaDespacho == "si" or (consultaDespacho == "SI") or (consultaDespacho == "Si")):

            clearConsole()                                                                 #borra consola

            comunasPrint(listado,comunas,comunaPrecio)                                     #muestra lista de comunas
            
            userSelect = input("Indique la comuna a la que desea despachar: ")             #consulta
            userSelect = int(userSelect)
            
            if (userSelect >= 1) and (userSelect <= 5):                                    #verifica que el usuario ingrese en el rango
                comunaDespacho = (comunas[(userSelect - 1)])                               #Busca en la tabla comunas y guarda en comunaDespacho
                precioDespacho = (comunaPrecio[(userSelect - 1)])                          #Busca en la tabla comunas y guarda en precioDespacho
                condicion = 1                                                              #resetea la condicion
            else:
                clearConsole()                                                             #borra consola
                print("COMUNA INGRESADA NO VALIDA, VUELVA A INTENTARLO")                   #imprime error
                time.sleep(1)                                                              #pausa para lectura
        else:
            precioDespacho = 0                                                              #setea el precioDespacho
            condicion = 1                                                                   #resetea la condicion
        clearConsole()                                                                      #borra consola
    return precioDespacho
