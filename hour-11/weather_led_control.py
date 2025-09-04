import network
import time
import urequests
from machine import Pin

# WiFi credentials - replace with your actual WiFi details
ssid = "my-wifi"
password = "Password1"

# LED setup - connected to GPIO pin 2 (built-in LED on most Pico boards)
led = Pin(2, Pin.OUT)

def connect():
    """Connect the Pico to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print("Connecting, please wait...")
        time.sleep(1)
    
    print("Connected! IP = ", wlan.ifconfig()[0])

def check_chennai_temperature():
    """Fetch weather data and check Chennai temperature"""
    try:
        # Weather API URL
        site = "https://hbdbc6t52wp5ylx6pupshtvldi0bjkwa.lambda-url.ap-south-1.on.aws/"
        print("Fetching weather data from:", site)
        
        # Make HTTP request
        r = urequests.get(site)
        weather_data = r.json()
        r.close()
        
        print("Weather data received:")
        
        # Find Chennai in the weather data
        chennai_temp = None
        for city_data in weather_data:
            print(f"- {city_data['city']}: {city_data['temperature']}°C ({city_data['weather']})")
            
            if city_data['city'] == "Chennai":
                chennai_temp = city_data['temperature']
        
        if chennai_temp is not None:
            print(f"\nChennai temperature: {chennai_temp}°C")
            
            # Check if temperature is greater than 30
            if chennai_temp > 30:
                led.on()
                print("🔴 LED ON - Chennai temperature is above 30°C!")
            else:
                led.off()
                print("🔵 LED OFF - Chennai temperature is 30°C or below")
        else:
            print("Chennai data not found in response")
            led.off()
            
    except Exception as e:
        print("Error fetching weather data:", e)
        led.off()

# Main program
try:
    # Connect to WiFi
    connect()
    
    # Check weather and control LED
    while True:
        check_chennai_temperature()
        print("Waiting 30 seconds before next check...\n")
        time.sleep(30)  # Check every 30 seconds
        
except KeyboardInterrupt:
    print("Program stopped by user")
    led.off()
except Exception as e:
    print("Program error:", e)
    led.off()