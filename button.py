import gpiozero

button = gpiozero.Button(17)

while True:
	if button.is_pressed:
		print ("Hello Nanna")
	else:
		print (".")

