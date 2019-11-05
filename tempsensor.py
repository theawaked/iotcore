
import bme280
import smbus2
from time import sleep
import database

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