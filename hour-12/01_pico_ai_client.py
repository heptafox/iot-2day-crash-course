# Hour 12 — Pico W: Sensor → Lambda → LLM decision → Actuators (Buzzer + LED)
# Beginner-friendly MicroPython script for Raspberry Pi Pico W
#
# What it does:
# 1. Connects to Wi-Fi (configure SSID & PASSWORD below)
# 2. Reads DHT11 temperature & humidity (GPIO15)
# 3. Sends JSON to an AWS Lambda Function URL (LAMBDA_URL)
# 4. Expects Lambda to return JSON like:
#    {"buzzer":"ON"|"OFF", "led":"ON"|"OFF", "reason":"short text"}
# 5. Acts on the response: turns buzzer and LED ON/OFF accordingly
#
# Wiring:
# - DHT11 DATA -> GPIO15
# - Buzzer + -> GPIO16 ; Buzzer - -> GND
# - LED: uses onboard LED if available, otherwise GPIO25 (connect external LED via resistor)

import network
import urequests
import ujson
import time
from machine import Pin
import dht

# ------------------- CONFIG -------------------
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"

LAMBDA_URL = "https://your-lambda-function-url-id.lambda-url.region.on.aws/"
# Example: "https://abcd1234.lambda-url.us-east-1.on.aws/"

DHT_PIN = 15        # DHT11 data pin
BUZZER_PIN = 16     # Buzzer control pin (active HIGH)
LED_FALLBACK_PIN = 25  # Fallback pin if onboard LED name isn't supported

READ_INTERVAL = 10  # seconds between readings
REQUEST_TIMEOUT = 10  # seconds for HTTP requests
# ----------------------------------------------

# Setup sensor and actuators
sensor = dht.DHT11(Pin(DHT_PIN))

buzzer = Pin(BUZZER_PIN, Pin.OUT)
# Try onboard LED first (Pin("LED") works on many Pico builds). Fallback to GP25.
try:
    led = Pin("LED", Pin.OUT)
except Exception:
    led = Pin(LED_FALLBACK_PIN, Pin.OUT)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("🔌 Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        timeout = 0
        while not wlan.isconnected():
            time.sleep(1)
            timeout += 1
            print("... waiting", timeout, "s")
            # Optional: break after long wait to avoid infinite loop in bad networks
            if timeout > 30:
                print("⚠️ Wi-Fi connect timeout. Retry after a short sleep.")
                timeout = 0
    print("✅ Wi-Fi connected. IP:", wlan.ifconfig()[0])

def post_sensor(temperature, humidity):
    """
    Send sensor JSON to Lambda and return parsed JSON response.
    On error return None.
    """
    try:
        payload = {"temperature": temperature, "humidity": humidity}
        body = ujson.dumps(payload)
        print("Sending:", body)
        resp = urequests.post(LAMBDA_URL,
                              headers={"Content-Type": "application/json"},
                              data=body,
                              timeout=REQUEST_TIMEOUT)
        # Read and parse JSON
        try:
            result = resp.json()
        except ValueError:
            print("Response not valid JSON:", resp.text)
            result = None
        resp.close()
        return result
    except Exception as e:
        print("HTTP error:", e)
        return None

def apply_actions(result):
    """
    Apply buzzer and led actions from Lambda result.
    Expected fields: 'buzzer' and 'led' with values 'ON' or 'OFF'.
    """
    if not isinstance(result, dict):
        print("Invalid action result:", result)
        safe_shutdown()
        return

    # Buzzer
    buz = result.get("buzzer")
    if buz == "ON":
        buzzer.on()
        print("🔊 Buzzer: ON")
    elif buz == "OFF":
        buzzer.off()
        print("🔊 Buzzer: OFF")
    else:
        print("🔕 Buzzer: unchanged")

    # LED
    led_cmd = result.get("led")
    if led_cmd == "ON":
        led.on()
        print("💡 LED: ON")
    elif led_cmd == "OFF":
        led.off()
        print("💡 LED: OFF")
    else:
        print("💡 LED: unchanged")

    # Optional: print reason if provided
    reason = result.get("reason")
    if reason:
        print("ℹ️ Reason:", reason)

def safe_shutdown():
    """
    Safe fallback: turn buzzer off and LED off to avoid unwanted alerts.
    """
    try:
        buzzer.off()
    except:
        pass
    try:
        led.off()
    except:
        pass
    print("✅ Safe fallback applied: buzzer OFF, LED OFF")

def main():
    connect_wifi()
    print("🔁 Starting sensor loop. Press Ctrl+C to stop.")
    while True:
        try:
            # Read sensor
            try:
                sensor.measure()
                t = sensor.temperature()
                h = sensor.humidity()
                print("Temperature:", t, "°C  💧 Humidity:", h, "%")
            except Exception as e:
                print("Sensor read error:", e)
                safe_shutdown()
                time.sleep(READ_INTERVAL)
                continue

            # Send to Lambda and get decision
            result = post_sensor(t, h)
            if result is None:
                print("No valid response from Lambda. Applying safe fallback.")
                safe_shutdown()
            else:
                apply_actions(result)

        except KeyboardInterrupt:
            print("Stopped by user.")
            safe_shutdown()
            break
        except Exception as e:
            print("Unexpected error in main loop:", e)
            safe_shutdown()

        time.sleep(READ_INTERVAL)

# Run
if __name__ == "__main__":
    main()
