# Complete Plant Monitor - DHT11 + Soil Moisture + Alerts
# Monitors temperature, humidity, and soil moisture for plants

import dht
from machine import Pin, ADC, PWM
import time

# Set up DHT11 sensor (temperature & humidity)
dht_sensor = dht.DHT11(Pin(15))

# Set up soil moisture sensor
moisture_sensor = ADC(Pin(26))

# Set up LED and buzzer for alerts
led = Pin(25, Pin.OUT)
buzzer = PWM(Pin(16))
buzzer.freq(1000)
buzzer.duty_u16(0)

# Thresholds for alerts
temp_max = 30      # Maximum temperature (°C)
temp_min = 15      # Minimum temperature (°C)
humidity_min = 40  # Minimum humidity (%)
moisture_min = 30  # Minimum soil moisture (%)

print("🌱 Complete Plant Monitor System")
print("Monitoring: Temperature, Humidity, Soil Moisture")
print(f"Alerts: Temp {temp_min}-{temp_max}°C, Humidity >{humidity_min}%, Moisture >{moisture_min}%")
print()

def sound_alert(beeps=1):
    """Sound buzzer alert"""
    for i in range(beeps):
        buzzer.duty_u16(32768)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        time.sleep(0.2)

def blink_led(blinks=1):
    """Blink LED"""
    for i in range(blinks):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)

while True:
    try:
        # Read DHT11 sensor
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        # Read soil moisture
        moisture_raw = moisture_sensor.read_u16()
        moisture_percent = 100 - ((moisture_raw / 65535) * 100)
        
        # Display all readings
        print(f"🌡️  Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌱 Soil Moisture: {moisture_percent:.1f}%")
        
        # Check for problems and alert
        alerts = []
        
        # Temperature checks
        if temperature > temp_max:
            alerts.append("🔥 TOO HOT!")
        elif temperature < temp_min:
            alerts.append("🧊 TOO COLD!")
        
        # Humidity check
        if humidity < humidity_min:
            alerts.append("🏜️  LOW HUMIDITY!")
        
        # Soil moisture check
        if moisture_percent < moisture_min:
            alerts.append("🚨 SOIL TOO DRY!")
        
        # Show alerts or OK status
        if alerts:
            print("⚠️  PLANT ALERTS:")
            for alert in alerts:
                print(f"   {alert}")
            
            # Sound buzzer and blink LED
            sound_alert(len(alerts))
            blink_led(len(alerts))
        else:
            print("✅ All conditions OK - Happy plant! 🌿")
            led.off()
        
        print("=" * 40)
        
    except OSError as e:
        print("❌ Sensor error - check wiring!")
        blink_led(5)  # 5 blinks for error
    
    time.sleep(5)  # Check every 5 seconds