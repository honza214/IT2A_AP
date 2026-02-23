from machine import Pin, PWM
from utime import sleep_ms, ticks_ms, ticks_diff

MAX_JAS = 65535
MIN_JAS = 0
FREKVENCE = 1500
PIN_TLACITKO = 10
PIN_TLACITKO2 = 11

tlacitko = Pin(PIN_TLACITKO, Pin.IN, Pin.PULL_DOWN)

tlacitko2 = Pin(PIN_TLACITKO2, Pin.IN, Pin.PULL_DOWN)

leds = []

for i in range(4):
    led = PWM(Pin(i))
    led.freq(FREKVENCE)
    led.duty_u16(MIN_JAS)
    leds.append(led)

#Wrappery
def zapni(led_obj):
    led_obj.duty_u16(MAX_JAS)

def vypni(led_obj):
        led_obj.duty_u16(MIN_JAS)

def zhasni_vse():
    for led in leds:
         vypni(led)   

def zapni_vse():
     for led in leds:
          zapni(led) 

def zapni_pozvolna(led_obj):
     for duty in range(MIN_JAS, MAX_JAS, 1500):
          led_obj.duty_u16(duty)
          sleep_ms(20)
            

def zhasni_pozvolna(led_obj):
     for duty in range(MAX_JAS, MIN_JAS, -1500):
        led_obj.duty_u16(duty)
        sleep_ms(20)

def hadR():
     zhasni_vse()
     for led in leds:
        zapni(led)
        sleep_ms(200)
        vypni(led)   

def hadL():
     zhasni_vse()
     for led in reversed(leds):
          zapni(led)  
          sleep_ms(200)
          vypni(led)    

def blik():
    zhasni_vse()
    sleep_ms(50)
    for led in leds:  
        zapni(led)
    sleep_ms(50)

def blik_obdva():
    zhasni_vse()
    for i in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)

    for i in range(2):
        for i, led in enumerate(leds):
            if i % 2 != 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)
                
def pozvolna_doprava_apakzhasni():
    try:
        for led in leds:
            zapni_pozvolna(led)
        for led in reversed(leds):
            zhasni_pozvolna(led)
            vypni(led)
    except KeyboardInterrupt:
            print("exit")


def pozvolna_doleva_apakzhasni():
    try:
        for led in reversed(leds):
            zapni_pozvolna(led)
        for led in leds:
            zhasni_pozvolna(led)
            vypni(led)
    except KeyboardInterrupt:
        print("exit")

    
def breath():
    pwm_leds = leds
    try:
        for duty in range(MIN_JAS, MAX_JAS, FREKVENCE):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            sleep_ms(50)
        for duty in range(MAX_JAS, MIN_JAS, -FREKVENCE):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            sleep_ms(50)
    except KeyboardInterrupt:
        print("exit")
        
def cekej(doba_ms):
    zacatek = ticks_ms()
    while ticks_diff(ticks_ms(), zacatek) < doba_ms:
        if tlacitko.value() == 1:
            sleep_ms(100)
            return True
        sleep_ms(1)
        return False
    
def zapni_pozvolna_(led_obj):
     for duty in range(MIN_JAS, MAX_JAS, 1500):
        led_obj.duty_u16(duty)
        if cekej(20) == True:
            return True
        return False
     
def zhasni_pozvolna_(led_obj):
    for duty in range(MAX_JAS, MIN_JAS, -1500):
        led_obj.duty_u16(duty)
        if cekej(20) == True:
            return True
        led_obj.duty_u16(0)
    return False
    
def hadR_():
     zhasni_vse()
     for led in leds:
        zapni(led)
        if cekej(200): return
        vypni(led)   

def hadL_():
     zhasni_vse()
     for led in reversed(leds):
        zapni(led)  
        if cekej(200) : return
        vypni(led)

def blik_obdva_():
    zhasni_vse()
    for i in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                zapni(led)
        if cekej(100) : return
        zhasni_vse()
        if cekej(100) : return

    for i in range(2):
        for i, led in enumerate(leds):
            if i % 2 != 0:
                zapni(led)
        if cekej(100) : return
        zhasni_vse()
        if cekej(100) : return
    
def breath_():
    pwm_leds = leds
    try:
        for duty in range(MIN_JAS, MAX_JAS, FREKVENCE):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            if cekej(20) : return
        for duty in range(MAX_JAS, MIN_JAS, -FREKVENCE):
            for pwm_led in pwm_leds:
                pwm_led.duty_u16(duty)
            if cekej(20) : return
    except KeyboardInterrupt:
        print("exit")

rezim = 0
POCET_REZIMU = 5


          
while True:
    try:
        if rezim == 0:
            hadL_()
        elif rezim == 1:
            hadR_()
        elif rezim == 2:
            blik()
        elif rezim == 3:
            blik_obdva_()
        elif rezim == 4:
            breath_()
        elif rezim == 5:
            pozvolna_doleva_apakzhasni()
            pozvolna_doprava_apakzhasni()

        if tlacitko.value() == 1:
            zhasni_vse()
            rezim = rezim +1
            print("Měním režim na: ", rezim)

        if rezim >= POCET_REZIMU:
            rezim = 0

        while tlacitko.value() == 1:
            sleep_ms(10)
        
        if tlacitko2.value() == 1:
            zhasni_vse()
            rezim = rezim -1
            print("Měním režim na: ", rezim)

        if rezim < 0:
            rezim = 5

        while tlacitko2.value() == 1:
            sleep_ms(10)

        
        #zapni(leds[0])
        #zhasni_vse()
        #zapni_vse()
        #zapni_pozvolna(leds[2])
        #zhasni_pozvolna(leds[2])
        #hadR()
        #hadL()
        #blik()
        #blik_obdva()
        #pozvolna_doprava_apakzhasni()
        #pozvolna_doleva_apakzhasni()
        #breath()
    except KeyboardInterrupt:
        print("exit")
        break


