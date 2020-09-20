from time import sleep
from gpiozero import Button
from controls.led import LED

button = Button("BOARD22", False, None)

def btn_press():
    print("Button pressed.")
    LED.led_display(2)

# Operation area.

print("Light test.")
LED.led_blink(5)

print("Test done, waiting for command...")
while True:
    button.wait_for_press()
    btn_press()
