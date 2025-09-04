# DHT11 with LED and Buzzer Alert - Beginner Program
# LED blinks and buzzer sounds when temperature gets too high

import dht
from machine import Pin, PWM
import time

# Set up DHT11 sensor on pin 15
sensor = dht.DHT11(Pin(15))

# Set up LED on pin 25 (onboard LED)
led = Pin(25, Pin.OUT)

# Set up buzzer on pin 16 (connect buzzer + to pin 16, - to GND)
buzzer = PWM(Pin(16))
buzzer.freq(1000)  # Set buzzer frequency to 1000 Hz
buzzer.duty_u16(0)  # Start with buzzer off

# Temperature threshold (change this number!)
temp_limit = 25  # LED blinks if temperature > 25°C

print("DHT11 Temperature Monitor with Buzzer")
print(f"LED will blink and buzzer will sound if temperature > {temp_limit}°C")
print("Buzzer connected to GPIO pin 16")
print()

while True:
    try:
        # Read sensor
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        
        # Print readings
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        
        # Check if temperature is too high
        if temperature > temp_limit:
            print("⚠️  HIGH TEMPERATURE ALERT!")
            # Blink LED and sound buzzer 3 times
            for i in range(3):
                led.on()
                buzzer.duty_u16(32768)  # Turn buzzer on (50% volume)
                time.sleep(0.3)
                led.off()
                buzzer.duty_u16(0)      # Turn buzzer off
                time.sleep(0.3)
        else:
            print("✅ Temperature OK")
            led.off()           # Make sure LED is off
            buzzer.duty_u16(0)  # Make sure buzzer is off
        
        print("---")
        
    except OSError as e:
        print("Sensor error - check wiring!")
        led.on()            # Turn LED on to show error
        buzzer.duty_u16(0)  # Make sure buzzer is off during error
    
    # Wait 3 seconds before next reading
    time.sleep(3)