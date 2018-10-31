import subprocess
import RPi.GPIO as GPIO
import time

#  cd tg
#  python led.py &
#  sudo bin/telegram-cli -k tg-server.pub 2>&1 | tee data.txt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


while True:
	if '/on' in open('data.txt').read():
		GPIO.output(18,GPIO.HIGH)
	elif '/off' in open('data.txt').read():
		GPIO.output(18,GPIO.LOW)

	open('data.txt', 'w').close()
	time.sleep(10)
