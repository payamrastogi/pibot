# Getting the libraries we need
from gpiozero import DistanceSensor
from time import sleep

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=4, echo=17)

while True:
	# Wait 1 seconds
	sleep(1)
	
	# Get the distance in metres
	distance = sensor.distance

	# But we want it in centimetres
	distance = sensor.distance * 100

	print("Distance : %.1f" % distance)

	# We would get a large decimal number so we will round it to 2 places
	#distance = round(sensor.distance, 2)

	# Print the information to the screen
	#print("Distance: {} cm".format(sensor.distance))