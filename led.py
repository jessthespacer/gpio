from gpiozero import LED
from time import sleep
led = LED(17)

for i in range(10):
	led.on()
	sleep(1)
	print "LED ON"
	led.off()
	sleep(1)
	print "LED OFF"
