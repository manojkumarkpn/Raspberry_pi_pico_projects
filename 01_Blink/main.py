from machine import Pin
import time
onboard_led = Pin(25, Pin.OUT)

while True:
    onboard_led.toggle()
    time.sleep(1)
