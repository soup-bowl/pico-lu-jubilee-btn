from machine import Pin, Timer
import time

tube_led = Pin(22, Pin.OUT)
tube_btn = Pin(21, Pin.IN, Pin.PULL_UP)
sys_led  = Pin(25, Pin.OUT)
timer    = Timer();

def tick(timer):
    global sys_led
    sys_led.toggle()
   
#timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

for x in range(5):
  tube_led.value(1)
  time.sleep(0.25)
  tube_led.value(0)
  time.sleep(0.25)

while True:
    first = tube_btn.value()
    time.sleep(0.01)
    second = tube_btn.value()
    if first and not second:
        print('Button pressed.')
        tube_led.value(1)
    elif not first and second:
        print('Button released.')
        tube_led.value(0)
