from machine import Pin, PWM
from utime import sleep_ms

# --- KONSTANTY A NASTAVENÍ ---
MAX_JAS = 65535  # Maximální hodnota pro PWM (100% svit)
MIN_JAS = 0      # Zhasnuto
FREKVENCE = 1000 # Hz --> kolikrát za vteřinu se stihne rozsvítit a zhasnout

# ---------------------------- Inicializace (Vše je PWM) -----------------------------
leds = []

# Vytvoříme rovnou PWM objekty a uložíme je do seznamu
for i in range(4):
    p = PWM(Pin(i))
    p.freq(FREKVENCE)
    p.duty_u16(MIN_JAS) # Pro jistotu zhasneme
    leds.append(p)

# ---------------------------- Wrappery (Pomocné funkce) -----------------------------
# Tyto funkce nám nahrazují .on() a .off()

def zapni(led_obj):
    """Rozsvítí PWM ledku na maximum"""
    led_obj.duty_u16(MAX_JAS)

def vypni(led_obj):
    """Zhasne PWM ledku"""
    led_obj.duty_u16(MIN_JAS)

def zhasni_vse():
    """Zhasne všechny LED v poli"""
    for led in leds:
        vypni(led)
def zapni_pozvolna(led_obj):
    for duty in range(MIN_JAS, MAX_JAS, 1500):       
        led_obj.duty_u16(duty)
        sleep_ms(20)

def vypni_pozvolna(led_obj):
    for duty in range(MAX_JAS, MIN_JAS, -1500):       
        led_obj.duty_u16(duty)
        sleep_ms(20)
    led_obj.duty_u16(0)

# ----------------------------- Animační funkce ----------------------------------
def hadR():
    zhasni_vse()
    for led in leds:
        zapni(led)      # Použití wrapperu
        sleep_ms(200)
        vypni(led)      # Použití wrapperu

def hadL():
    zhasni_vse()
    for led in reversed(leds):
        zapni(led)
        sleep_ms(200)
        vypni(led)

def leftRight():
    hadL()
    hadR()

def blik():
    zhasni_vse()
    for led in leds:
        zapni(led)
    sleep_ms(50)
    zhasni_vse() # Tady stačí zavolat hromadné zhasnutí
    sleep_ms(50)

def blik_ob():
    zhasni_vse()
    # 1. Část - Sudé
    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)

    # 2. Část - Liché
    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 != 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)      

# --------------------------- PWM animace-----------------------------------
def breath():
    # Zde už není potřeba žádná inicializace ani deinit!
    # Piny jsou připravené.
    
    # Nádech (z tmy do světla)
    for duty in range(MIN_JAS, MAX_JAS, 1500):
        for led in leds:
            led.duty_u16(duty) # Zde přistupujeme přímo k hodnotě
        sleep_ms(20) 
        
    # Výdech (ze světla do tmy)
    for duty in range(MAX_JAS, MIN_JAS, -1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(20)

def PWM_Right_On():
    zhasni_vse()
    for led in leds:
        zapni_pozvolna(led)      # Použití wrapperu

def PWM_Right_Off():
    for led in leds:
        vypni_pozvolna(led)      # Použití wrapperu

def PWM_Left_On():
    zhasni_vse()
    for led in reversed(leds):
      zapni_pozvolna(led)

def PWM_Left_Off():
    for led in reversed(leds):
      vypni_pozvolna(led)

# ---------------------------- Main část -----------------------------------
        
while True:
    try:
        hadL() 
        breath()   
        hadR()
        blik_ob()
        for i in range (10):
            blik()
        PWM_Right_On()
        PWM_Right_Off()
        PWM_Left_On()
        PWM_Left_Off()
    except KeyboardInterrupt:
        zhasni_vse()
        # Není potřeba dělat deinit, prostě jen zhasneme a ukončíme
        print("Exit")
        break