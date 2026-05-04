from machine import Pin
from utime import sleep_ms

btnPins = [0,1,2,3]
buttons = []
lastStates = []

for pinNum in btnPins:
    btn = Pin(pinNum, Pin.IN, Pin.PULL_DOWN)
    buttons.append(btn)
    lastStates.append(0)
while True:
    for i in range(len(buttons)):
        currentState = buttons[i].value()   
        if currentState != lastStates[i]:
            if currentState == 1:
                print(f"Tlačítko {btnPins[i]} je stisknuto")
            else:
                print(f"Tlačítko {btnPins[i]} je uvolněno")
            lastStates[i] = currentState
        sleep_ms(20)

