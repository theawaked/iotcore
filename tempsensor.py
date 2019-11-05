
import bme280
import smbus2
from time import sleep
import database

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)

    temperature = bme280_data.temperature
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    
    print(humidity, pressure, temperature)
    database.insertdata(temperature, humidity)
    database.printdb
    sleep(1)