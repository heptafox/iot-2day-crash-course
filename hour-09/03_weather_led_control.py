import network
import time
import urequests
import ujson as json
from machine import Pin

# WiFi credentials - replace with your actual WiFi details
ssid = "my-wifi"
password = "Password1"

# LED setup - change the pin according to your board
led = Pin(2, Pin.OUT)

# Lambda base URL (no query params here)
BASE_URL = "https://hbdbc6t52wp5ylx6pupshtvldi0bjkwa.lambda-url.ap-south-1.on.aws/"

# City to request
CITY = "Chennai"

def connect():
    """Connect the Pico to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print("Connecting, please wait...")
            time.sleep(1)
    print("Connected! IP =", wlan.ifconfig()[0])

def get_city_weather(city):
    """Call Lambda with ?city=<city> and return JSON dict or None on error"""
    url = "{}?city={}".format(BASE_URL, city)
    print("Requesting:", url)
    try:
        resp = urequests.get(url)
    except Exception as e:
        print("HTTP request failed:", e)
        return None

    try:
        # Check status code if available
        if hasattr(resp, "status_code"):
            code = resp.status_code
        elif hasattr(resp, "status"):
            code = resp.status  # some ports use resp.status
        else:
            code = None

        if code is not None and code != 200:
            print("Non-200 response:", code)
            text = resp.text if hasattr(resp, "text") else None
            print("Body:", text)
            resp.close()
            return None

        data = resp.json()
    except ValueError as e:
        # JSON decoding failed
        print("Failed to decode JSON:", e)
        try:
            print("Raw response:", resp.text)
        except:
            pass
        resp.close()
        return None
    except Exception as e:
        print("Error reading response:", e)
        resp.close()
        return None

    resp.close()
    return data

def handle_weather_response(data):
    """Process returned data and control LED"""
    if not data:
        print("No data received.")
        led.off()
        return

    # The Lambda returns either a city dict or {"error": "..."} when city not found
    if isinstance(data, dict) and data.get("error"):
        print("Lambda returned error:", data.get("error"))
        led.off()
        return

    # If it's a dict with city and temperature
    if isinstance(data, dict) and "city" in data and "temperature" in data:
        city = data.get("city")
        temp = data.get("temperature")
        weather = data.get("weather", "")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Weather:", weather)
        try:
            if float(temp) > 30.0:
                led.on()
                print("🔴 LED ON - temperature above 30°C")
            else:
                led.off()
                print("🔵 LED OFF - temperature 30°C or below")
        except Exception as e:
            print("Temperature value error:", e)
            led.off()
        return

    # If Lambda returned the whole list (fallback), try to find the city locally
    if isinstance(data, list):
        found = False
        for city_data in data:
            if isinstance(city_data, dict) and city_data.get("city", "").lower() == CITY.lower():
                handle_weather_response(city_data)
                found = True
                break
        if not found:
            print("City not found in returned list.")
            led.off()
        return

    # Unexpected format
    print("Unexpected response format:", data)
    led.off()

# Main program
try:
    connect()
    while True:
        weather = get_city_weather(CITY)
        handle_weather_response(weather)

        # Wait before next check
        print("Waiting 30 seconds before next check...\n")
        time.sleep(30)

except KeyboardInterrupt:
    print("Program stopped by user")
    led.off()
except Exception as e:
    print("Program error:", e)
    led.off()

#https://hbdbc6t52wp5ylx6pupshtvldi0bjkwa.lambda-url.ap-south-1.on.aws/?city=Delhi