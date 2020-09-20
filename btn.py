from time import sleep
from gpiozero import Button, LED

button = Button("BOARD22", False)
light  = LED("BOARD7")

print("Light test.")
for x in range(5):
    light.on()
    sleep(0.25)
    light.off()
    sleep(0.25)

print("Test done, waiting for command...")
while True:
    button.wait_for_press()
    for x in range(3):
        print("Button pressed.")
        light.on()
        sleep(1)
    light.off()
