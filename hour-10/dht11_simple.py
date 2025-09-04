# Simple DHT11 - Beginner Program
# Connect DHT11 data pin to GPIO 15

import dht
from machine import Pin
import time

# Set up DHT11 sensor
sensor = dht.DHT11(Pin(15))

# Read temperature and humidity forever
while True:
    try:
        sensor.measure()  # Take reading
        
        temp = sensor.temperature()    # Get temperature
        humid = sensor.humidity()      # Get humidity
        
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humid}%")
        print("---")
        
    except:
        print("Sensor error!")
    
    time.sleep(2)