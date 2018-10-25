import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
pinsOut = [14, 15, 18]
pinsIn = [23]
state = 0

def cb(channel):
	if GPIO.input(pinsIn[0]) == GPIO.HIGH:
		print("Switch HIGH")
	else:
		print("Switch LOW")

try:
	GPIO.setmode(GPIO.BCM)

	for pin in pinsOut:
		GPIO.setup(pin, GPIO.OUT)
	GPIO.setup(pinsIn[0], GPIO.IN)

	GPIO.add_event_detect(pinsIn[0], GPIO.BOTH, callback=cb)

	while True:
		if state == 0:
			GPIO.output(pinsOut[-1], GPIO.LOW)
			GPIO.output(pinsOut[0], GPIO.HIGH)
		elif state == 1:
			GPIO.output(pinsOut[0], GPIO.LOW)
			GPIO.output(pinsOut[1], GPIO.HIGH)
		elif state == 2:
			GPIO.output(pinsOut[1], GPIO.LOW)
			GPIO.output(pinsOut[2], GPIO.HIGH)
		else:
			for pin in pinsOut:
				GPIO.output(pin, GPIO.LOW)
		sleep(3)

		if GPIO.input(pinsIn[0]) == GPIO.LOW and state == 0:
			state = 1
		elif state == 1:
			state = 2
		elif state == 2:
			state = 0

except KeyboardInterrupt:
	print("KeyboardInterrupt detected.")
finally:
	print("Exiting.")
	GPIO.cleanup()
