import serial
import paho.mqtt.client as mqtt

#ARDUINO
puerto = serial.Serial('/dev/ttyACM0', 9600)
entradas = 0
salidas = 0
total = 0;

def conexionExitosa (client, userdata, flags, rc):
	#print("Conectados con exito a ioticos.org")
	client.subscribe("TM")
	client.publish("TM", "Se ha conectado")

def informe ():
	cliente.publish('TM', "-----REPORTE-----")
	cliente.publish('TM','Total entradas: ' + str(entradas))
	cliente.publish('TM','Total salidas: ' + str(salidas))
	cliente.publish('TM','Personas dentro: ' + str(total))
	cliente.publish('TM',"-----------------\n")

#MQTT
cliente = mqtt.Client()
#cliente.connect("localhost", 1883, 60)

######
cliente.on_connect = conexionExitosa
cliente.username_pw_set("okvhngmo", "9cMFCvD33apD")
cliente.connect("tailor.cloudmqtt.com", 15541, 60)

while True:
	cliente.publish("TM","Hola")
	lectura = puerto.readline()
	#print(lectura)
	valor = lectura.rstrip()
	#print(valor)

	#print(lectura.rstrip('\n'))

	if valor == b'1':
		print("Notificando entrada...")
		#cliente.connect("tailor.cloudmqtt.com", 15541, 60)
		cliente.publish("TM", "Se ha detectado una entrada")
		
		entradas += 1;
		total += 1;
		informe()
	else:
		if valor == b'0':
			if total != 0:
				print("Notificando salida...")
				#cliente.connect("localhost", 1883, 60)
				#cliente.connect("tailor.cloudmqtt.com", 15541, 60)
				cliente.publish("TM", "Se ha detectado una salida")
				salidas += 1;
				total -= 1;
				informe()
	

