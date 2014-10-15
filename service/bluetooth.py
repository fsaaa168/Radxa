import serial
import os
bluetooth = serial.Serial(0,9600)
#ser.isOpen()
while True:
	recieve = bluetooth.readline()
	recieve = recieve[0:-2]
	result = os.popen(recieve).read()
	bluetooth.write(result)
	bluetooth.write('---------------------------------------------------------\n')
