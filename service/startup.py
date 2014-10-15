import time
import os
import subprocess

#INIT
#def init():
#	return

#BLUE_LED
def start_blue_led():
	blue_process = subprocess.Popen(['python' , '/home/rock/service/BLUE_LED.py'])
	pid = '%d' %blue_process.pid
	file = open('/home/rock/service/PID/BLUE_LED_PID', 'w')
	file.write('BLUE_LED_PID = ')
	file.write(pid)
	file.write('\n')
	file.close()
	return blue_process

#GREEN_LED
def start_green_led():
	green_process = subprocess.Popen(['python' , '/home/rock/service/GREEN_LED.py'])
	pid = '%d' %green_process.pid
	file = open('/home/rock/service/PID/GREEN_LED_PID', 'w')
	file.write('GREEN_LED_PID = ')
	file.write(pid)
	file.write('\n')
	file.close()
	return green_process

#BLUETOOTH
def start_bluetooth():
	bluetooth_process = subprocess.Popen(['python' , '/home/rock/service/bluetooth.py'])
	pid = '%d' %bluetooth_process.pid
	file = open('/home/rock/service/PID/BLUETOOTH_PID', 'w')
	file.write('BLUETOOTH_PID = ')
	file.write(pid)
	file.write('\n')
	file.close()
	return bluetooth_process
#init process
blue_led_process = start_blue_led()
green_led_process = start_green_led()
#bluetooth_process = start_bluetooth()

#Main Loop of Service
while True:
	if blue_led_process.poll():
		blue_led_process = start_blue_led()
	if green_led_process.poll():
		green_led_process = start_green_led()
	#if bluetooth_process.poll():
		#bluetooth_process = start_bluetooth()

