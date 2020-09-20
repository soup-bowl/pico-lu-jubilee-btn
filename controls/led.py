from time import sleep
from gpiozero import LED

light = LED("BOARD7")

class LED:
    def led_display(length):
        light.on()
        sleep(length)
        light.off()

    def led_blink(count):
        for x in range(count):
            light.on()
            sleep(0.25)
            light.off()
            sleep(0.25)

