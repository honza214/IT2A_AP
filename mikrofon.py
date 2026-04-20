from machine import Pin,  ADC
from utime import sleep_ms, ticks_ms, ticks_diff

mic = ADC(26)

leds = []
for i in range(4):
    leds.append(Pin(i, Pin.OUT))
THRESHOLDS = [160,450,600,650]
avg = []

def soundLed(level):
    for i in range(len(THRESHOLDS)):
        if level > THRESHOLDS[i]:
            leds[i].on()
        else:
            leds[i].off

while True:
    try:
        """val = mic.read_u16()
            print(val)
            sleep_ms(100)"""
        
        maxVal = 0
        minVal = 65536

        StartTime = ticks_ms()
        while ticks_diff(ticks_ms(), StartTime) < 50:
            val = mic.read_u16()

            if val < minVal: minVal = val
            if val > minVal: maxVal = val

        peaktoPeak = maxVal - minVal

        if len(avg) > 5:
            avg.pop(0)
        avg.append(peaktoPeak)
        hodnota = sum(avg)/len(avg)


        soundLed(hodnota)
        print(f"Min: {minVal} Max: {maxVal} Rozdil: {peaktoPeak} Prumer: {hodnota}")
        sleep_ms(100)
        

    except KeyboardInterrupt:
        for led in leds:
            led.off()
        break
