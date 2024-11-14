from machine import Pin

pin = Pin(13, Pin.OUT)

for i in range(0,5):
    pin.value(0)
    time.sleep(1)
    pin.value(1)
    time.sleep(1)