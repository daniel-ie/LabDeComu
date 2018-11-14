import subprocess
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)


def write2db():
	date = subprocess.Popen("echo `date` >> db.txt", shell=True)

while True:
	# Check the state of the tank
	stateEmpty = GPIO.input(23) 
	stateFull = GPIO.input(24)

	if '/on' in open('data.txt').read():
		GPIO.output(18,GPIO.HIGH)
	elif '/off' in open('data.txt').read():
		GPIO.output(18,GPIO.LOW)

	if stateEmpty == 0: # empty tank	
		subprocess.Popen(['sudo bin/telegram-cli -k tg-server.pub -e "msg SIMONA   Advertencia tanque vacio!"'], shell=True)
		write2db()	

	if '/level' in open('data.txt').read():
		if stateFull == 0: # half done tank
			subprocess.Popen(['sudo bin/telegram-cli -k tg-server.pub -e "msg SIMONA   Tanque medio lleno!"'], shell=True) 
		if stateFull == 1: # full tank
			subprocess.Popen(['sudo bin/telegram-cli -k tg-server.pub -e "msg SIMONA   Tanque lleno!"'], shell=True)

	if '/historial' in open('data.txt').read():
		subprocess.Popen(['sudo bin/telegram-cli -k tg-server.pub -e "send_file SIMONA   db.txt"'], shell=True)
	
	
	open('data.txt', 'w').close()


	#print(str(GPIO.input(23)))
	time.sleep(10)

