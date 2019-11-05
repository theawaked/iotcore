# import config as config
# import RPi.GPIO as GPIO
# from Adafruit_BME280 import *

# sensor = BME280(address = config.I2C_ADDRESS)

# while True:
#           temperature = sensor.read_temperature()
#           humidity = sensor.read_humidity()
#           pressure = sensor.read_pressure()
#           print(temperature,humidity)

#           time.sleep(config.MESSAGE_TIMESPAN / 1000.0)


import bme280
import smbus2
from time import sleep

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)