import subprocess
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(23, GPIO.IN)



while True:
	if '/on' in open('data.txt').read():
		GPIO.output(18,GPIO.HIGH)
	elif '/off' in open('data.txt').read():
		GPIO.output(18,GPIO.LOW)

	open('data.txt', 'w').close()

	# Check the state of the tank
	state = GPIO.input(23) 

	if state == 0: # empty tank
		subprocess.Popen(['sudo bin/telegram-cli -k tg-server.pub -e "msg SIMONA   Advertencia tanque vacio"
'], shell=True)

	#print(str(GPIO.input(23)))
	time.sleep(10)
