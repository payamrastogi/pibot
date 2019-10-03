from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(6, 13, 19, 26)
delay = 0.07
while True:
	leds.value = (1, 0, 0, 0)
	sleep(delay)
	leds.value = (0, 1, 0, 0)
	sleep(delay)
	leds.value = (0, 0, 1, 0)
	sleep(delay)
	leds.value = (0, 0, 0, 1)
	sleep(delay)
	leds.value = (0, 0, 1, 0)
	sleep(delay)
	leds.value = (0, 1, 0, 0)
	sleep(delay)