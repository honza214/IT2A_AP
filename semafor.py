from machine import Pin
from utime import sleep

cervena = Pin(0, Pin.OUT)
oranzova = Pin(1, Pin.OUT)
zelena = Pin(2, Pin.OUT)

while True:
    try:
        cervena.value(1)
        oranzova.value(0)
        zelena.value(0)
        sleep(2)

        cervena.value(0)
        oranzova.value(1)
        zelena.value(0)
        sleep(2)

        cervena.value(0)
        oranzova.value(0)
        zelena.value(1)
        sleep(2)

    except KeyboardInterrupt:
        print("Konec semaforu")