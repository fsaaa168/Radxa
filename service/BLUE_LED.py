import time
import os

CLASS_NOW = 0

def BLUE_LED_ENABLE():
	file = open('/sys/class/gpio/export', 'w')
	file.write('174')
	file.close()
	file = open('/sys/class/gpio/gpio174/direction', 'w')
	file.write("out")
	file.close()

def BLUE_LED_STATE(state):    #0 as off; 1 as on;
	if state == 0:
		file = open('/sys/class/gpio/gpio174/value', 'w')
		file.write('1')
		file.close()
	else:
		file = open('/sys/class/gpio/gpio174/value', 'w')
		file.write('0')
		file.close()

def BLUE_LED_GRADUALLY_ON():
	step = 0.0001
	for i in range(0,100):
		BLUE_LED_STATE(1)
		time.sleep(0.000+step)
		BLUE_LED_STATE(0)
		time.sleep(0.010-step)
		step+=0.0001
	BLUE_LED_STATE(1)

def BLUE_LED_GRADUALLY_OFF():
	step = 0.0001
	for i in range(0,100):
		BLUE_LED_STATE(0)
		time.sleep(0.000+step)
		BLUE_LED_STATE(1)
		time.sleep(0.010-step)
		step+=0.0001
	BLUE_LED_STATE(0)

def BLUE_LED_PWM(CLASS, TIME):#CLASS_min/max : 0/1000,TIME:ms
	ms = TIME/1000.00
	CLASS_NOW = CLASS
	#print CLASS_NOW
	if CLASS == 0:
		BLUE_LED_STATE(0)
		time.sleep(ms)
	elif CLASS == 1000:
		BLUE_LED_STATE(1)
		time.sleep(ms)
	else:
		step = 0.00001
		start = time.time()
		sleep_1 = 0.00+step*CLASS
		sleep_0 = 0.01-step*CLASS
		while True:
			if time.time() - start >= ms:
				break
			BLUE_LED_STATE(1)
			time.sleep(sleep_1)
			BLUE_LED_STATE(0)
			time.sleep(sleep_0)

def BLUE_LED_GRADUALLY_PWM(START, END, SPEED):#CLASS_min/max : 0/1000;SPEED_min:1
	if START<= END:
		for i in range(START, END + 1, SPEED):
			BLUE_LED_PWM(i,10)
	else:
		for i in range(START, END - 1, -SPEED):
			BLUE_LED_PWM(i,10)

if os.path.exists(r'/sys/class/gpio/gpio174/direction') == False:
	BLUE_LED_ENABLE()

def main_loop():
	while True:
		BLUE_LED_GRADUALLY_PWM(0, 1000, 10)
		BLUE_LED_STATE(1)
		time.sleep(0.5)
		BLUE_LED_GRADUALLY_PWM(1000, 0, 10)
		time.sleep(1.5)

if __name__ == '__main__':
	main_loop()