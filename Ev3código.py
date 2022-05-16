#Imports que usamos para el código
from typing_extensions import Self
from tabulate import  tabulate
import csv
from collections import namedtuple
import sys
import sqlite3
from sqlite3 import Error

#Se creó una lista vacía para el almacenamiento de los datos que se vayan a registrar
lista = []

#Se define la variable para la función de registrar un servicio
def RegistroServicio():
    while True:
#Después de esto, procede a preguntar los datos a registrar al usuario
        Detalles1=input("Equipo/s a registrar:")
        Detalles2=input("Describe los detalles del equipo a registrar:")
        Registro1=input("Introduce el folio: ")
        Registro2=input("Introduce la fecha de registro (ddmmaa): ")
        Registro3=input("Introduce el nombre del cliente: ")
        Registro4= float (input("Introduce el monto cobrado : "))
        iva = Registro4 * 0.16
        funcionregistro = (Detalles1, Detalles2, Registro1, Registro2, Registro3, Registro4 + iva)
#Aquí empieza el proceso para crear una base de datos
        try:
            with sqlite3.connect("PrimerIntentoDemo.db") as conn:
                mi_cursor = conn.cursor()
#Se insertan las variables anteriormente registradas para almacenarlas
                valores = (Registro1, Detalles1, Detalles2, Registro2, Registro3, Registro4 + iva)
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS proyecto (folio INTEGER PRIMARY KEY, Equipo TEXT NOT NULL, Detalles TEXT NOT NULL, Fecha DATE NOT NULL, Nombre TEXT NOT NULL, Monto INTEGER NOT NULL);")
                print("Registro creado exitosamente")
                mi_cursor.execute("INSERT INTO proyecto VALUES(?,?,?,?,?,?)", valores)
                print("Registro agregado exitosamente")
#En caso de ocurrir un error con el almacenamiento, se despliega el siguiente mensaje
        except Error as e:
                print (e)
        except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
#Se cierra la base de datos y se guarda el registro
        finally:
                conn.close()
#En esta línea se avisa al usuario sobre el porcentaje de iva del monto cobrado
                print("(Aviso: el IVA de su monto es(16%): $", iva)
                print("Su monto total a pagar es:","$",Registro4 + iva)
                break

#Después de insertar los datos, se crea una tupla donde se conservan para la impresión de los detalles del registro
    funcionregistro = (Detalles1, Detalles2, Registro1, Registro2, Registro3, Registro4 + iva)
    print ("--------------------Registro exitoso----------------------")
    print ("------------------Detalles del registro:-----------------")
    print ("Equipo/s:", funcionregistro[0])
    print ("Detalles equipo:", funcionregistro[1])
    print ("Folio:", funcionregistro[2])
    print ("Fecha registro:", funcionregistro[3])
    print ("Nombre del cliente:", funcionregistro[4])
    print ("Precio total: $", funcionregistro[5])
#En esta línea se avisa al usuario sobre el porcentaje de iva del monto cobrado






#Se define una variable para la función de consultar un servicio con folio
def ConsultaServicio():
    while True:
        NodeFolio=input("Introduce el folio del servicio a consultar (ddmmaa):")
#Si el dato insertado es un folio anteriormente registrado y que se encuentre en la lista principal,
#se procede a imprimir y tabular el servicio consultado
        if NodeFolio==(lista[2]):
            rios2 = [[lista]]
        print(tabulate(rios2))
        break

#Se define una variable y se pregunta al usuario la fecha del servicio a consultar
def ServicioFecha():
    while True:
#Si hay más de un servicio con la misma fecha, también se consultarán
#Al igual que la consulta con folio, la fecha también debe de estar dentro de la lista principal
#para que se pueda realizar la consulta
        Fec=input("Introduce la fecha del servicio/s a consultar (ddmmaa):")
        if Fec==(lista[3]):
            rios1 = [[lista]]
        print(tabulate(rios1))
        break




#Este es el menú que se desplegará al ejecutar al código
while True:
    print(" ")
    print("-"*50)
    print("Servicio de soporte técnico")
    print("-"*50)
    print("[a] Registrar un servicio")
    print("[b] Consultar un servicio")
    print("[f] Consultar los servicios realizados en una fecha específica")
    print("[x] Salir")
    opcion=input("Qué opción deseas: ")
    if (opcion=="x"):
        break
    if (opcion=="a"):
        RegistroServicio()
    if (opcion=="b"):
        ConsultaServicio()
    if (opcion=="f"):
        ServicioFecha()