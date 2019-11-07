
import bme280
import smbus2
from time import sleep
import database

import paho.mqtt.client as mqtt

#connecten met broker(webserver)
broker="192.168.1.10"
port=1883



client = mqtt.Client(client_id=”raspgerben”, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client.on_connect = on_connect
client.on_message = on_message
#test
# broker = iot.eclipse.org
# port = 1883 #SSL = 883

client.connect(broker, port)

# Aanpassen naar temp e humidity
client.publish("topic","ON")

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def readandlog():
          
          bme280_data = bme280.sample(bus,address)

          temperature = bme280_data.temperature
          humidity  = bme280_data.humidity
          pressure  = bme280_data.pressure
          
          print(temperature, humidity)
          database.insertdata(temperature, humidity)
          database.printdb()
          

def main():
          while True:
                    readandlog()
                    sleep(20)

main()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

## kijken of crontab nog nuttig is.