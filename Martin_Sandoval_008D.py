import csv
import time
import os
from random import*

with open("pedidos.csv","w",newline='') as pedidos_csv:
    registro_csv = csv.writer(pedidos_csv)
    registro_csv.writerow(["Nro.Ped""\t","Cliente""\t","Direccion""\t","Sector""\t\t","Saco 5KG""\t","Saco 10KG""\t","Saco 20 KG"])
    registro_csv.writerow(["15" , "miguel cortes" , "Los canelos#1042" , "San Bernardo" , "1" , "1" , "0"])


def menu():
    
    while True:
        try:
            print(('''------Bienvenido a Catpremiun------\n\nPorfavor elija una de las opciones:\n\n1.-Registro de pedidos\n2.-Lista de todos los pedidos\n3.-Imprimir hoja de ruta\n4.-Salir del programa'''))
            opc=int(input("Respuesta:"))
        
                    
            if opc==1:
                nru=randint(1,1000)
                os.system("cls")
                time.sleep(1)
                print(f'Su numero de pedido es: {nru}')
                time.sleep(3)
                os.system("cls")
                nombre=input("Ingrese su nombre : ")
                os.system("cls")
                time.sleep(0.5)
                direccion=input("Ingrese su direccion: ")
                os.system("cls")
                time.sleep(0.5)
                sector=input("Ingrese su sector: ")
                os.system("cls")
                time.sleep(0.5)
                while True:
                    try:
                        saco5=int(input("¿Cuantos de 5kg?: "))
                        os.system("cls")
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("Ingrese un valor valido")
                        
                while True:
                    try:
                        saco10=int(input("¿Cuantos de 10kg: "))
                        os.system("cls")
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("Ingrese un valor valido")
                        
                while True:        
                    try:     
                        saco20=int(input("¿Cuantos de 20kg?: "))
                        os.system("cls")
                        print("DATOS GUARDADOS EXITOSAMENTE")
                        time.sleep(2)
                        os.system("cls")
                        break
                    except ValueError:
                        print("Ingrese un valor valido")
                        
            

                a=([nru,nombre,direccion,sector,saco5,saco10,saco20])
                registro_pedidos(a)
            elif opc==2:
                os.system("cls")
                lectura_pedidos()
                time.sleep(7)
                os.system("cls")
                

            elif opc==3:
                os.system("cls")
                hojaderuta() 
                time.sleep(7)
                os.system("cls")

            elif opc==4:
                adiosmundo()
                break
            else:
                print("INGRESE UN NUMERO ENTRE 1 Y 4")
        except ValueError:
            os.system("cls")
            print("INSERTE UN VALOR VALIDO")
            time.sleep(2)
            os.system("cls")
                   





def registro_pedidos(data):
     with open("pedidos.csv","a",newline="") as pedidos_csv:
          nuevopedido_csv = csv.writer(pedidos_csv)
          nuevopedido_csv.writerow(data)
        

def lectura_pedidos():
     with open("pedidos.csv","r",newline="") as pedidos_csv:
             lectura_csv = csv.reader(pedidos_csv)
             for fila in pedidos_csv:
                  print(fila)

def hojaderuta():
     with open("hojaderuta.txt","w") as ruta_txt:
          ruta_txt='''los sectores disponibles son:\n1.-San Bernardo\n2.-La Pintana\n3.-Buin\n4.-Puente Alto\n5.-El bosque'''
          print(ruta_txt)


def adiosmundo():
     print("Un gusto, Hasta la proxima")
     


menu()