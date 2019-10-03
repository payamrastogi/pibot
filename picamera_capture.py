from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(2)
camera = PiCamera()

def capture():
	timestamp = datetime.now().isoformat()
	camera.capture('/home/pi/robot/pics/%s.jpg' % timestamp)
	print('Hello')

button.when_pressed = capture

pause()