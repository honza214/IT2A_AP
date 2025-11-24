from machine import Pin
from utime import sleep
led = Pin(0, Pin.OUT)
print("LED zacina blikat...")
while True:
    try:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
    except KeyboardInterrupt:
        break
print("hotovo")