# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:45:08 2020

@author: Antonio Fernández Ares (antares@ugr.es)

Ejemplo Sockets: Servidor
"""

import socket

host = socket.gethostname()

port = 12345

BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
	socket_tcp.bind((host,port))
	socket_tcp.listen(5)
	conn,addr = socket_tcp.accept()

	with conn:
		print("[*] Conexión establecida")
		while True:
			data = conn.recv(BUFFER_SIZE)
			if not data:
				break
			else:
				print("[*] Datos recibidos {}".format(data.decode('utf-8')))
			conn.send(data) #Mandamos un echo


#¿Qué cambiamos para que funcione en otra máquina?
#El cliente puede comenzar un envío de  un número indeterminado de bytes en  cualquier momento (asíncrono).
#¿Cómo sabe el servidor que el envío  de datos ha finalizado y que no quedan  datos pendientes?
#Normalmente, un servidor maneja  múltiples conexiones al mismo tiempo  mediante concurrencia o paralelismo.  Véase la implementación para  conexiones múltiples en  https://unipython.com/programacion-  de-redes-en-python-sockets/
