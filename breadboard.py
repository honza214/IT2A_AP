from machine import Pin
from utime import sleep

leds = Pin(0, Pin.OUT)
print("LED zacina blikat...")
while True:
    try:
        leds.on()
        sleep(0.5)  
        leds.off()
        sleep(0.5)
    except KeyboardInterrupt:
        print("Ocekavany konec")
        break
print("Hotovo.")
