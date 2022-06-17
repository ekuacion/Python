#========================================================================================================================================
# Servidor en python TCP/IP
#========================================================================================================================================
# Librerias
import socket
import json
import time

#========================================================================================================================================
# Variables y Definiciones
ip = ''                             # Escucha toas las conexiones entrantes
puerto = 6000                       # Puerto de conexion 6000
dataConection = (ip, puerto)        # Definimos conexion data
conexionesMaximas = 5               # Podran conectarse 5 clientes como maximo
arr1 = "2"
arr = bytes(arr1, 'utf-8')
#----------------------------------------------------------------------------------------------------------------------------------------
# Creamos el servidor.
# socket.AF_INET                                                # Para indicar que utilizaremos Ipv4
# socket.SOCK_STREAM                                            # Para utilizar TCP/IP (no udp)
Servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # Creamos el servidor
Servidor.bind(dataConection)                                    # Asignamos los valores del servidor
Servidor.listen(conexionesMaximas)                              # Asignamos el número máximo de conexiones
#----------------------------------------------------------------------------------------------------------------------------------------
# Estableciendo conexiones 
print("Esperando conexiones en %s:%s" %(ip, puerto))                    # Espera conexiones entrantes
cliente, direccion = Servidor.accept()                                  # Acepta las conexiones entrantes 
print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))   # Establece conexiones 

#========================================================================================================================================
#Bucle de escucha. En Ã©l indicamos la forma de actuar al recibir las tramas del cliente
datos = cliente.recv(1024)                  # El número indica el número maximo de bytes
print(datos)
while True:
    rList = [1, 2]
    arr = bytearray(rList)
    print(arr)
    time.sleep(2)
    #cliente.send(arr)
    #print("RECIBIDO: %s" %msg) 
    if datos == "exit":                         # Si no hay datos, entonces ...
        cliente.send("exit")                    # Envia exit al cliente
        break                                   # Cierra el ciclo while
    
print("CONEXIÓN CERRADA ")                      # Imprime conexion cerrada 
Servidor.close()                                # Cierra el servidor
