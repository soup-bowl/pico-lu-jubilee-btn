import RPi.GPIO as GPIO
from gpiozero import Button

def button_callback(channel):
    print("Open door.")

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

GPIO.add_event_detect(22,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
