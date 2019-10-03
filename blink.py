import gpiozero
import time

led = gpiozero.LED(4)

while True:
	led.on()
	time.sleep(2)
	led.off()
	time.sleep(1)
	led.on()
	time.sleep(1)

