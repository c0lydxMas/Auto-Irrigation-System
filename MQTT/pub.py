import serial
import time
import paho.mqtt.client as paho
from paho import mqtt
from secret import *

# Initialize serial port
serialPort = serial.Serial(
    port="COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)

# Used to hold data coming over serial port
serialString = ""

# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(USERNAME, PASSWORD)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HIVEMQ_CLOUD, 8883)


while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:
        # Read data out of the buffer
        serialString = serialPort.readline()
        # Decode the data
        mqtt_msg = serialString.decode("Ascii")
        print(mqtt_msg)
        # Single publish to HiveMQ Broker
        client.publish("khanhbq/soilmoisture", payload=mqtt_msg, qos=1)
        # Sleep 2 seconds
        time.sleep(0.2)
