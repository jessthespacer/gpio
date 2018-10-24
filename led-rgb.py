import RPi.GPIO as GPIO
from time import sleep, time
import math

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins = [14, 15, 18]
freq = 100            # [Hz]
pwm = [0, 0, 0]
col = [255, 0, 255]

try:
	for i, out in enumerate(pins):
		GPIO.setup(out, GPIO.OUT)
		pwm[i] = GPIO.PWM(out, freq)
		pwm[i].start(col[i]/255.0 * 100)
	while True:
		pass
except KeyboardInterrupt:
	print("Keyboard interrupt detected.")
finally:
	print("Exiting.")
	for i, out in enumerate(pins):
		pwm[i].stop()
	GPIO.cleanup()
