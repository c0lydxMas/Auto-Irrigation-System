import sys
sys.path.insert(0, 'E:\Dev\EmbeddedSystem\Server')
import datetime
import paho.mqtt.client as paho
from paho import mqtt
from secret import *
from db import *


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print((msg.payload).decode('UTF-8'))
    insertData([datetime.datetime.now(), (msg.payload).decode('UTF-8')])

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(USERNAME, PASSWORD)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HIVEMQ_CLOUD, 8883)

# setting callbacks, separate functions for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to topic
client.subscribe("khanhbq/soilmoisture", qos=1)

# loop_forever
client.loop_forever()