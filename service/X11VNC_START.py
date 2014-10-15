import os
import subprocess
#os.system('x11vnc -forever')
x11vnc_process = subprocess.Popen(['x11vnc' , '-forever'])
pid = '%d' %x11vnc_process.pid
file = open('/home/rock/service/PID.conf', 'a')
file.write('X11VNC_PID = ')
file.write(pid)
file.write('\n')
file.close()