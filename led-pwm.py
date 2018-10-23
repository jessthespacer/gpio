import RPi.GPIO as GPIO
from time import sleep, time
import math

def sawtooth(x):
	return x - math.floor(x)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

start = time()
freq = 100.0		# [Hz]
period = 1/freq		# [s]
t = 0
duration = 5

wavetype = {"sine":		lambda x: 0.5 * (math.sin(x * 2 * math.pi) + 1), \
	    "linear off":	lambda x: (duration - x)/duration, \
	    "linear on":	lambda x: x/duration, \
	    "sawtooth":		lambda x: sawtooth(x * 2 * math.pi)}
wavefunc = wavetype["sawtooth"]
dc = 0

try:
	while t < duration:
		dc = wavefunc(0.1 * t)
		GPIO.output(17, GPIO.HIGH)
		sleep(period * dc)
		GPIO.output(17, GPIO.LOW)
		sleep(period * (1 - dc))
		t = time() - start
except KeyboardInterrupt:
	print("Keyboard interrupt detected.")
finally:
	print("Exiting.")
	GPIO.cleanup()
