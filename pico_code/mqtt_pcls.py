import network, rp2, machine, time, ujson, json
from umqtt_simple import MQTTClient

"""
MQTT client class for the Pico (by Norman & Samuel)

This module provides a MQTT client class for the Raspberry Pi Pico W that handles:
- WiFi connection with status LED feedback
- MQTT broker connection and message handling
- Basic publish/subscribe functionality
- JSON message encoding/decoding

The LED gives Feedback during the connection
- Fast blink: Error, not (yet) connected
- Slow blink: Connection in progress
- LED off: Connected
- LED on: Got stuck
"""

# Define status messages
WLAN_STATUS_MESSAGES = {
    network.STAT_IDLE: "Status: Idle (no connection activity).",  # 0
    network.STAT_CONNECTING: "Status: Connection in progress.",  # 1
    2: "Status: Connect to AP, waitung for IP address.", # 2 (not 100% clear whether text is correct)
    network.STAT_WRONG_PASSWORD: "Error: Incorrect password.", # -1
    network.STAT_NO_AP_FOUND: "Error: No access point found.", # -2
    network.STAT_CONNECT_FAIL: "Error: Connection failed due to other problems.", # -3
    network.STAT_GOT_IP: "Status: Connected successfully with an IP address." # 3
}

class MQTT:

    def __init__(self, wlan_ssid, wlan_password, mqtt_address, wifi_country='CH', **mqtt_kwargs):
        """
        Initialize the MQTT client
        
        Args:
            wlan_ssid (str): SSID of the Wi-Fi network
            wlan_password (str): Password of the Wi-Fi network
            mqtt_address (str): Address of the MQTT broker
            wifi_country (str): Country code for the Wi-Fi network (default: 'CH')
            **mqtt_kwargs: Additional keyword arguments for the MQTT client
        """
        self.wlan_ssid = wlan_ssid
        self.wlan_password = wlan_password
        self.mqtt_address = mqtt_address
        self.subscribed_topics = []

        # Set the Wi-Fi country
        rp2.country(wifi_country)

        # initiate wlan client
        self.wlan = network.WLAN(network.STA_IF)

        # initiate mqtt client
        self.mqtt_client = MQTTClient(self.client_id(), mqtt_address, **mqtt_kwargs)
        self.mqtt_client.set_callback(self._mqtt_callback)
        self._last_received_topic = None
        self._last_received_msg = None

        # initiate LED on pico
        self.LED = machine.Pin("LED", machine.Pin.OUT)
        self.LED.off()

        # connect
        self.connect()
        
    def connect(self):
        """
        Connect to the Wi-Fi network and the MQTT broker

        Returns:
            bool: True if successful, False otherwise
        """
        if not self.ensure_wlan():
            return False
        elif not self.connect_mqtt():
            return False
        else:
            for topic in self.subscribed_topics:
                if not self.subscribe(topic):
                    return False
            return True

    def subscribe(self, topic):
        """
        Subscribe to a topic

        Args:
            topic (str): Topic to subscribe to

        Returns:
            bool: True if successful, False otherwise
        """
        if topic not in self.subscribed_topics:
            self.subscribed_topics.append(topic)
        try:
            self.mqtt_client.subscribe(topic)
            return True
        except Exception as e:
            print(f"MQTT Error: Unable to subscribe to topic {topic} - {e}")
            return self.connect()

    def get_last_msg(self):
        """
        Get the last received message

        Returns:
            Last received message
        """
        _, msg = self.get_last_topic_and_msg()
        return msg
    
    def get_last_topic_and_msg(self): 
        """
        Get the last received topic and message

        Returns:
            Last received topic and message
        """
        try:
            self.mqtt_client.check_msg()
        except Exception as e:
            print(f"MQTT Error: Unable to check messages - {e}")
            self.connect()
            self.mqtt_client.check_msg()

        last_topic = self._last_received_topic
        last_msg = self._last_received_msg
        self._last_received_topic = None
        self._last_received_msg = None
        return last_topic, last_msg

    def send_msg(self, topic, msg): 
        """
        Send a message to a topic

        Args:
            topic (str): Topic to send the message to
            msg (dict, list, tuple): Message to send

        Returns:
            bool: True if successful, False otherwise
        """
        if type(msg) in [dict, list, tuple]:
            msg = json.dumps(msg)
        try:
            self.mqtt_client.publish(topic, msg)
            return True
        except Exception as e:
            print(f"MQTT Error: Unable to send message - {e}")
            if self.connect():
                self.mqtt_client.publish(topic, msg)
                return True
            else:
                return False

    # ---- Helper functions ----

    def _mqtt_callback(self, topic, msg):    
        """
        Callback function for incoming messages

        Args:
            topic: Topic of the incoming message
            msg : Message of the incoming message
        """
        self._last_received_topic = topic.decode()
        self._last_received_msg = json.loads(msg)

    def client_id(self):
        """
        Create a unique identifier for the MQTT client
        """
        pattern = "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}"
        return pattern.format(*machine.unique_id())

    def blink_led(self, frequency_hz=5, duration_seconds=1):
        """
        Blink the LED at the specified frequency for the given duration.
        
        Args:
            frequency_hz (float): Frequency of blinking in Hz (default: 5)
            duration_seconds (float): Total duration to blink in seconds (default: 1)
        """
        cycles = int(duration_seconds * frequency_hz)
        half_period = 0.5 / frequency_hz
        
        for _ in range(cycles):
            self.LED.on()
            time.sleep(half_period)
            self.LED.off() 
            time.sleep(half_period)
        self.LED.off()

    def ensure_wlan(self, max_retries=100, sleep_seconds=2):
        """
        Ensure the Wi-Fi connection is established

        Args:
            max_retries (int): Maximum number of retries (default: 100)
            sleep_seconds (float): Time to sleep between retries in seconds (default: 2)

        Returns:
            bool: True if successful, False otherwise
        """
        # WLAN should already be initialized in __init__
        self.wlan.active(True)

        # Set Wi-Fi power-saving mode off
        self.wlan.config(pm=0xa11140)

        # Start the connection process
        self.wlan.connect(self.wlan_ssid, self.wlan_password)
        retries = 0

        # Retry loop
        while not self.wlan.isconnected() and retries < max_retries:
            status = self.wlan.status()
            status_msg = WLAN_STATUS_MESSAGES.get(status, f"Unknown status code {status}")
            print(f"Retry {retries}/{max_retries}: {self.wlan_ssid} connected: {self.wlan.isconnected()}, status: {status}, {status_msg}")

            retries += 1

            if status < 0:
                self.wlan.connect(self.wlan_ssid, self.wlan_password)
                self.blink_led(frequency_hz=10, duration_seconds=sleep_seconds)  # fast blinking
            else:
                self.blink_led(frequency_hz=2, duration_seconds=sleep_seconds)  # slow blinking
            
        # Final check
        if self.wlan.isconnected():
            print(f"Successfully connected to {self.wlan_ssid}!")
            print(f"IP Configuration: {self.wlan.ifconfig()}")
            try:
                # Retrieve and print RSSI if supported
                rssi = self.wlan.status('rssi')
                print(f"Signal Strength (RSSI): {rssi} dBm")
            except Exception as e:
                print(f"Unable to retrieve RSSI: {e}")
            return True
        else:
            print(f"Failed to connect to {self.wlan_ssid} after multiple attempts.")
            return False

    def connect_mqtt(self):
        """
        Initialize MQTT client and connect to broker

        Returns:
            bool: True if successful, False otherwise
        """
        self.LED.on()
        try:
            self.mqtt_client.connect()
            print(f"Connected to MQTT broker at {self.mqtt_address}")
            self.LED.off()
            return True
        except Exception as e:
            print(f"Failed to create MQTT client: {e}")
            self.LED.off()  
            return False

