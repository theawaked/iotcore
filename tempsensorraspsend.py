
import bme280
import smbus2
from time import sleep
import database

#import paho.mqtt.client as mqtt

#ip webserver
#broker_address="192.168.1.184" 

#Client(client_id=”raspgerben”, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)

#maken van client
#client =mqtt.Client(client_name)

#connecten met broker(webserver)
# broker="192.168.1.184"
# port=1883
#client.connect(broker, port)

# Aanpassen naar temp e humidity
# client.publish("topic","ON")

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

## kijken of crontab nog nuttig is.