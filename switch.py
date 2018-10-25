import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)
pinsOut = [14, 15, 18]
pinsIn = [23]


def callout(channel):
	if GPIO.input(pinsIn[0]) == GPIO.HIGH:
		print("1 @ " + str(datetime.now()))
	else:
		print("0 @ " + str(datetime.now()))

try:
	GPIO.setmode(GPIO.BCM)

	for pin in pinsOut:
	        GPIO.setup(pin, GPIO.OUT)

	for pin in pinsIn:
        	GPIO.setup(pin, GPIO.IN)

	GPIO.add_event_detect(pinsIn[0], GPIO.BOTH, callback=callout)

	while True:
		pass
except KeyboardInterrupt:
	print("KeyboardInterrupt detected")
finally:
	GPIO.cleanup()
	print("Exiting.")
