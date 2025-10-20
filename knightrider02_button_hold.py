from machine import Pin
from utime import sleep

start_pin = 0
end_pin = 3
pos = start_pin
ink = 1
pins=[]
buzzer = Pin(4,Pin.OUT)
button = Pin(5,Pin.IN,Pin.PULL_DOWN)

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i,Pin.OUT))


print("Jizda zacina!!!")

while True:
    try:
        if button.value() == 1:
            pins[pos].on()
            sleep(0.001)
            pins[pos].off()
             

        
        
            pos += ink
            if (pos > end_pin) or (pos < start_pin):
                ink *= -1
                pos += 2*ink
                buzzer.on()
                sleep(0.001)
                buzzer.off()
        else:
            sleep(0.01)

    
    except KeyboardInterrupt:
        for pin in pins:
            pin.off()
        break