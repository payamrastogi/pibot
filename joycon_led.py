#import evdev
from evdev import InputDevice, categorize, ecodes

from gpiozero import LEDBoard

leds = LEDBoard(6, 13, 19, 26)

#creates object 'joycon' to store the data
joycon = InputDevice('/dev/input/event2')

#prints out device info at start
print(joycon)

#evdev takes care of polling the controller in loop
for event in joycon.read_loop():
	#filters by event type
	#print('type '+ str(event.type))
	#print('code '+ str(event.code))
	#print('value '+ str(event.value))
	if event.code == 17:
		if event.value == -1:
			print('up')
			leds.value = (1, 0, 0, 0)
		elif event.value == 1:
			print('down')
			leds.value = (0, 0, 0, 1)
	elif event.code == 16:
		if event.value == -1:
			print('left')
			leds.value = (0, 1, 0, 0)
		elif event.value == 1:
			print('right')
			leds.value = (0, 0, 1, 0)
	elif event.code == 305 and event.value == 1:
		print('A')
	elif event.code == 304 and event.value == 1:
		print('B')
	elif event.code == 306 and event.value == 1:
		print('Y')
	elif event.code == 307 and event.value == 1:
		print('X')
	elif event.code == 313 and event.value == 1:
		print('+')
		leds.value = (1, 1, 1, 1)
	elif event.code == 316 and event.value == 1:
		print('Home')
		leds.value = (0, 0, 0, 0)

