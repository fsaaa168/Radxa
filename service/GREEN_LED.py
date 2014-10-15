import time
import os

def GREEN_LED_ENABLE():
	file = open('/sys/class/gpio/export', 'w')
	file.write('172')
	file.close()
	file = open('/sys/class/gpio/gpio172/direction', 'w')
	file.write("out")
	file.close()

def GREEN_LED_STATE(state):    #0 as off; 1 as on;
	if state == 0:
		file = open('/sys/class/gpio/gpio172/value', 'w')
		file.write('1')
		file.close()
	else:
		file = open('/sys/class/gpio/gpio172/value', 'w')
		file.write('0')
		file.close()

if os.path.exists(r'/sys/class/gpio/gpio172/direction') == False:
	GREEN_LED_ENABLE()

GREEN_LED_STATE(1)
while True:
	GREEN_LED_STATE(0)
	time.sleep(1.95)
	GREEN_LED_STATE(1)
	time.sleep(0.05)