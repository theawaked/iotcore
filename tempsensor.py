import config as config
import RPi.GPIO as GPIO
from Adafruit_BME280 import *

sensor = BME280(address = config.I2C_ADDRESS)

while True:
          temperature = sensor.read_temperature()
          humidity = sensor.read_humidity()
          pressure = sensor.read_pressure()
          print(temperature,pressure)

          time.sleep(config.MESSAGE_TIMESPAN / 1000.0)
