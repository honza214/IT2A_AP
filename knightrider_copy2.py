from machine import Pin
from utime import sleep, ticks_ms, ticks_diff

start_pin = 0
end_pin = 3
pos = start_pin
ink = 1
pins=[]
buzzer = Pin(4,Pin.OUT)
button = Pin(5,Pin.IN,Pin.PULL_DOWN)
speed = 200
lastState = 0
lastchange = ticks_ms() 

for i in range(start_pin, end_pin +1):
    pins.append(Pin(i,Pin.OUT))


print("Jizda zacina!!!")

while True:
    now= ticks_ms()
    try:
        pins[pos].on()
        currentState = button.value()
        if currentState == 1 and lastState == 0 and speed <= 2000:
            speed += 100
            print(speed)
        lastState = currentState

        if speed < 2000 :
            if ticks_diff(now,lastchange) >= speed:
                pins[pos].off()
                lastchange = now
            pos += ink


            if (pos > end_pin) or (pos < start_pin):
                ink *= -1
                pos += 2*ink
                buzzer.on()
                sleep(0.1)
                buzzer.off()
        else:
            pins[pos-ink].off()
            print("dosaženo maximální ryhclosti") 

    
    except KeyboardInterrupt:
        for pin in pins:
            pin.off()
        break