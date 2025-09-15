# Simple Soil Moisture - Beginner Program
# Connect sensor A0 to pin 26, VCC to 3.3V, GND to GND

from machine import Pin, ADC
import time

# Set up soil moisture sensor
moisture = ADC(Pin(26))

# Read soil moisture forever
while True:
    # Read sensor (0 = very wet, 65535 = very dry)
    reading = moisture.read_u16()
    
    print(f"Soil reading: {reading}")
    
    if reading > 40000:
        print("Soil is DRY - needs water!")
    else:
        print("Soil is WET - good!")
    
    time.sleep(2)