#Programa cliente pc 

#Librerias
import socket
import time

#Variables
ipServidor = "localhost" #es lo mismo que "localhost" o "0.0.0.0"
puertoServidor = 10000
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
        msg = str(i)
        b = bytes(msg)
        cliente.sendall(b)
        time.sleep(1)
    if i == 200:
        break;
        
        
print("------- CONEXIÓN CERRADA ---------")

#_________________________________________________________________________

cliente.close()
