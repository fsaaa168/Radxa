import time
import os
import subprocess

dir(subprocess)
Popen = subprocess.Popen(["date"])
Popen.pid

#kill process
#kill blue_led_process
file = open('/home/rock/service/PID/BLUE_LED_PID', 'rb')
line = file.readline()
pid = line[-5:-1]
os.system('kill ' + pid)
print line[0:-7] + 'has been killed, pid = ' + pid + '\n'
file.close()

#kill green_led_process
file = open('/home/rock/service/PID/GREEN_LED_PID', 'rb')
line = file.readline()
pid = line[-5:-1]
os.system('kill ' + pid)
print line[0:-7] + 'has been killed, pid = ' + pid + '\n'
file.close()

#kill bluetooth_process
file = open('/home/rock/service/PID/BLUETOOTH_PID', 'rb')
line = file.readline()
pid = line[-5:-1]
os.system('kill ' + pid)
print line[0:-7] + 'has been killed, pid = ' + pid + '\n'
file.close()



#BLUE_LED OFF
file = open('/sys/class/gpio/gpio174/value', 'w')
file.write('1')
file.close()

#GREEN_LED OFF
file = open('/sys/class/gpio/gpio172/value', 'w')
file.write('1')
file.close()

os.system('rm /home/rock/service/PID/BLUE_LED_PID')
os.system('rm /home/rock/service/PID/GREEN_LED_PID')
