
import time, network, rp2
from machine import I2C, Pin
from dht20 import DHT20 as DHT # Humidity and temperature sensor interface
from mqtt_pcls import MQTT

# ------ configs -----
# Wifi and MQTT setting
SSID =  "iot-ZHAW"
PASSWORD = "5ne25-5568-zFhHZ"

# MQTT brokers
#MQTT_ADDRESS    = "test.mosquitto.org"      # URL of the MQTT broker server
MQTT_ADDRESS = "broker.hivemq.com"        # URL of the MQTT broker server

# MQTT topics
MQTT_BASE_TOPIC = "zhaw/pcls/vonwemel" # Eigener Surfername
MQTT_SEND_TOPIC = MQTT_BASE_TOPIC + "/from_pico"
MQTT_RECEIVE_TOPIC = MQTT_BASE_TOPIC + "/to_pico"

# ----- main -----
def main():

    # Initialize MQTT client
    mqtt = MQTT(SSID, PASSWORD, MQTT_ADDRESS)
    mqtt.subscribe(MQTT_RECEIVE_TOPIC)

    #Setup LED:
    led = Pin(16, mode=Pin.OUT)

    # Setup humidity and temperature sensor
    # dht = DHT(18)
    i2c1 = I2C(1, 
            sda=Pin(6, mode=Pin.IN, pull=Pin.PULL_UP), 
            scl=Pin(7, mode=Pin.IN, pull=Pin.PULL_UP),
            freq=400000)
    sensor = DHT(i2c1)
    
    print("MQTT demo is on!")
    print("Waiting for data...")
    
    while True:
        # measure temperature and humidity
        sensor_values = {
            'temp': sensor.temperature(),
            'humid' : sensor.humidity()
        }

        # send sensor values with MQTT
        mqtt.send_msg(MQTT_SEND_TOPIC, sensor_values)
                
        # Check for incoming messages (from MQTT)
        msg = mqtt.get_last_msg()
        print(f"Last message: {msg}")
        if (msg is not None) and ('switch' in msg):
            if msg['switch']:
                led.on()
            else:
                led.off()

        # give it a break for a second
        time.sleep(1.0)


if __name__ == "__main__":
    main()
