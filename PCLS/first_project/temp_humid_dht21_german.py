###############################################################################
# PCLS / Physical Computing in Life Sciences
# Norman Juchler
###############################################################################


###############################################################################
# Demo für SCHWARZEN Humidity Sensor (v2.1)
###############################################################################

from lcd1602 import LCD1602      # Lädt die Klasse für den Display
from dht20 import DHT20 as DHT   # Lädt die Klasse für den DHT Sensor
from machine import (I2C, Pin,
                     ADC, PWM)   # Lädt die angegebenen Klassen der "machine" Bibliothek
from utime import sleep          # Lädt die "sleep" Funktion um den Code pausieren zu können

# Den Display hängen wir am I2C0 Port an.
# Den Sensor hängen wir am I2C1 Port an.
# Achtung: Pins müssen stimmen!
i2c0 = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
i2c1 = I2C(1,
           sda=Pin(6, mode=Pin.IN, pull=Pin.PULL_UP),
           scl=Pin(7, mode=Pin.IN, pull=Pin.PULL_UP),
           freq=400000)

sensor = DHT(i2c1)
sleep(2)
sensor.measure()

# Richtet den Display ein am Port I2C0
d = LCD1602(i2c0, 2, 16)

# Richtet den passiven Buzzer am digitalen Pin D16 an.
# Setze eine Frequenz von 500Hz
buzzer = PWM(Pin(16))  
buzzer.freq(500)      

while True:  # while-Schlaufe (folgender Codeblock läuft kontinuerlich)
    sensor.measure()                    # Temperatur und Feuchtigkeit messen
    sleep(1)                            # Code pausiert für eine 1 Sekunde
    temp = sensor.temperature()    
    hum = sensor.humidity()
    d.setCursor(0,0)                    # Setzt die Anzeigeposition auf (0,0) 
    d.print("Temp:  %3.1f" % temp)      # Zeigt die Temperatur an 
    d.setCursor(0,1)                    # Setzt die Anzeigeposition auf (0,1) 
    d.print("Humid: %3.1f" % hum)       # Zeigt die Feuchtigkeit an 

    if temp > 28 or hum > 80:
        buzzer.duty_u16(200)            # Schaltet den Buzzer ein (Zahl: Lautstärke)
    else:
        buzzer.duty_u16(0)              # Schaltet den Buzzer aus
    sleep(0.5)
