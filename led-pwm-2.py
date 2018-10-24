import RPi.GPIO as GPIO
from time import sleep, time
import math

def sawtooth(x):
	return x - math.floor(x)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins = [14, 15, 18]
freq = 20            # [Hz]
pwm = [None for i in range(len(pins))]
t = 0
duration = 20

wavetype = {"sine":		lambda x: 0.5 * (math.sin(x * 2 * math.pi) + 1), \
	    "linear off":	lambda x: (duration - x)/duration, \
	    "linear on":	lambda x: x/duration, \
	    "sawtooth":		lambda x: sawtooth(x * 2 * math.pi)}
wavefunc = [wavetype["sawtooth"], wavetype["linear off"], wavetype["sine"]]

try:
	for i, out in enumerate(pins):
		GPIO.setup(out, GPIO.OUT)
		pwm[i] = GPIO.PWM(out, freq)
		pwm[i].start(0)
	start = time()
	while t < duration:
		t = time() - start
		for i, out in enumerate(pins):
			pwm[i].ChangeDutyCycle(wavefunc[i](t) * 100)
except KeyboardInterrupt:
	print("Keyboard interrupt detected.")
finally:
	print("Exiting.")
	GPIO.cleanup()
