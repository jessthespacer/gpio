import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def red(on):
	if on:
		GPIO.output(2, GPIO.HIGH)
	else:
		GPIO.output(2, GPIO.LOW)

def yellow(on):
	if on:
		GPIO.output(3, GPIO.HIGH)
	else:
		GPIO.output(3, GPIO.LOW)

def green(on):
	if on:
		GPIO.output(4, GPIO.HIGH)
	else:
		GPIO.output(4, GPIO.LOW)

try:
	while True:
		red(True)
		sleep(1)
		red(False)
		yellow(True)
		sleep(1)
		yellow(False)
		green(True)
		sleep(1)
		green(False)
except KeyboardInterrupt:
	print("KeyboardInterrupt detected.")
finally:
	print("Exiting.")
	GPIO.cleanup()
