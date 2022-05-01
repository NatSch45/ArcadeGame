import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

BUTTON_PIN = 38

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

run = True
while run:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button has been pushed !")