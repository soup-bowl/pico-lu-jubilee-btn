from machine import Pin
import time
from led import LED

tube_btn = Pin(21, Pin.IN, Pin.PULL_UP)
sys_led  = Pin(25, Pin.OUT)

print('Blinking LED to power check (no LED? Check LED batteries and/or script).')
LED.led_blink(5)

print('Blink code finish - Listening for presses.')
while True:
    first = tube_btn.value()
    time.sleep(0.01)
    second = tube_btn.value()
    if first and not second:
        print('Button pressed.')
        LED.led_display(2)
    elif not first and second:
        print('Button released.')
