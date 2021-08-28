from machine import Pin
from time import sleep

tube_led = Pin(22, Pin.OUT)

class LED():
    def led_display(length):
        global tube_led

        tube_led.value(1)
        sleep(length)
        tube_led.value(0)

    def led_blink(count):
        global tube_led

        for x in range(count):
            tube_led.value(1)
            sleep(0.25)
            tube_led.value(0)
            sleep(0.25)
