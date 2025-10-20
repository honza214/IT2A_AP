from machine import Pin
from utime import sleep

start_pin = 0
end_pin = 3
pos = start_pin
ink = 1
pins=[]

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i,Pin.OUT))


print("Jizda zacina!!!")

while True:
    try:
        
        pins[pos].on()
        sleep(0.2)
        pins[pos].off()
        
        pos += ink
        if (pos > end_pin) or (pos < start_pin):
            ink *= -1
            pos += 2*ink
            
        

            
    except KeyboardInterrupt:
        for pin in pins:
            pin.off()
        print("Konec")
        break