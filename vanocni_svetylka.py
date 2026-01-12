from machine import Pin
from utime import sleep_ms

leds = []

for i in range(4):
    leds.append(Pin(i, Pin.OUT))

def zhasni():
    for led in leds:
        led.off()

def blik():
    zhasni()
    sleep_ms(50)
    for led in leds:
        led.on()
    sleep_ms(50)

def hadR():
    zhasni()
    for led in leds:
        led.on()   
        sleep_ms(200)
        led.off()

def hadL():
    zhasni()
    for led in reversed(leds):
        led.on()
        sleep_ms(200)
        led.off()

def leftright():
    hadL()
    hadR()

def blikOb():
    zhasni()
    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                led.on()
        sleep_ms(100)
        zhasni()
        sleep_ms(100)

    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 1:
                led.on()
        sleep_ms(100)
        zhasni()
        sleep_ms(100)

while True:
    try:
        blikOb()
        #leftright()#
        #hadR()#
        #hadL()#
        #blik()#
    except KeyboardInterrupt:
        zhasni()
        break