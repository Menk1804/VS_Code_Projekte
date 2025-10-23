from lcd1602 import LCD1602   # Load the class for the display
from dht import DHT11 as DHT  # Load the class for the DHT sensor
from machine import I2C, Pin  # Required connection objects
from utime import sleep       # sleep() allows to stop the code for a bit

# We can connect the display to one of the two I2C ports
i2c0 = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
# i2c1 = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)  # Alternative port if needed

# Let's create the display instance
d = LCD1602(i2c0, 2, 16)

# Let's initialize the DHT sensor for the digital port D18
sensor = DHT(Pin(18))
sleep(0.5)

while True:
    sensor.measure()          # Measure sensor data
    sleep(1)                  # Sleep a bit
    
    temp = sensor.temperature()  # Get temperature
    hum = sensor.humidity()      # Get humidity
    
    d.setCursor(0, 0)             # Place cursor at (0,0)
    d.print("Temp: %3.1f" % temp) # Print temperature
    d.setCursor(0, 1)             # Place cursor at (0,1)
    d.print("Humid: %3.1f" % hum) # Print humidity
    
    sleep(1)                      # Wait before next reading
