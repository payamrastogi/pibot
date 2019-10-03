#import evdev
from evdev import InputDevice, categorize, ecodes

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
		elif event.value == 1:
			print('down')
	elif event.code == 16:
		if event.value == -1:
			print('left')
		elif event.value == 1:
			print('right')
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
	elif event.code == 316 and event.value == 1:
		print('Home')

