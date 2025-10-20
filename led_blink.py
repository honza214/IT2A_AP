from machine import Pin
from utime import sleep


pin0= Pin(0,Pin.OUT)


print("zaciname")
while True:
    try:
        pin0.toggle()
        sleep(10)
    except KeyboardInterrupt:
        print("konec")
        
        break