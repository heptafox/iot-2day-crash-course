# DHT11 Temperature & Humidity Sensor - Beginner Program
# Reads temperature and humidity from DHT11 sensor

import dht
from machine import Pin
import time

# Connect DHT11 sensor to pin 15
# Wiring:
# DHT11 VCC → 3.3V on Pico
# DHT11 GND → GND on Pico  
# DHT11 Data → GPIO pin 15
sensor = dht.DHT11(Pin(15))

print("DHT11 Sensor Reading")
print("Try blowing on sensor to see humidity change!")
print("Try touching sensor to see temperature change!")
print()

while True:
    try:
        # Read sensor (this takes a moment)
        sensor.measure()
        
        # Get temperature in Celsius
        temperature = sensor.temperature()
        
        # Get humidity percentage
        humidity = sensor.humidity()
        
        # Print the readings
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print("---")
        
    except OSError as e:
        print("Failed to read sensor - check wiring!")
    
    # Wait 2 seconds before next reading
    time.sleep(2)