from machine import Pin, PWM
from utime import sleep_ms

MAX_JAS = 65535
MIN_JAS = 0
FREKVENCE = 1000

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
     for j in range(2):
          for i, led in enumerate(leds):
            if i % 2 == 0:
                zapni(led)
            sleep_ms(100)
            zhasni_vse()
            sleep_ms(100)
                
                
    
          
while True:
    try:
        #zapni(leds[0])
        #zhasni_vse()
        #zapni_vse()
        #zapni_pozvolna(leds[2])
        #zhasni_pozvolna(leds[2])
        #hadR()
        #hadL()
        #blik()
        blik_obdva()
        
    except KeyboardInterrupt:
        print("exit")
        break