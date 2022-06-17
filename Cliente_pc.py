#Programa cliente pc 

#Librerias
import socket
import time
import json 

#Variables
ipServidor = "0.0.0.0" #es lo mismo que "localhost" o "0.0.0.0"
puertoServidor = 6000
BUFFER_SIZE = 1000

#Creando Cliente
cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectando Cliente a pc
cliente.connect((ipServidor,puertoServidor))
print("Conectado con el servidor ---> %s:%s" %(ipServidor, puertoServidor))

#_________________________________________________________________________
#Enviando datos
while True:
    i=1
    for i in range(200):
        i = str(i)
        b = bytes(i,'utf-8')
        cliente.sendall(b)
        datos=cliente.recv(1024)
        msg=datos.decode('ascii')
        time.sleep(0.5)
        #print(i)
        print(datos)
    if i == 200:
        break;   
print("------- CONEXIÓN CERRADA ---------")

#_________________________________________________________________________

cliente.close()
