import time
import os

def RED_LED_ENABLE():
	file = open('/sys/class/gpio/export', 'w')
	file.write('175')
	file.close()
	file = open('/sys/class/gpio/gpio175/direction', 'w')
	file.write("out")
	file.close()

def RED_LED_STATE(state):    #0 as off; 1 as on;
	if state == 0:
		file = open('/sys/class/gpio/gpio175/value', 'w')
		file.write('0')
		file.close()
	else:
		file = open('/sys/class/gpio/gpio175/value', 'w')
		file.write('1')
		file.close()

if os.path.exists(r'/sys/class/gpio/gpio175/direction') == False:
	RED_LED_ENABLE()

while True:
	RED_LED_STATE(0)
	time.sleep(1)
	RED_LED_STATE(1)
	time.sleep(1)