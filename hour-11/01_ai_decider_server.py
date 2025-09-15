import network
import urequests
import ujson
import time
from machine import Pin
import dht

# 🔹 Step 1: Wi-Fi settings
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

# 🔹 Step 2: AWS Lambda URL
LAMBDA_URL = "https://5eoypyonje3u3qzuvlj4k45l2q0cwwzt3.lambda-url.ap-south-1.on.aws/"

# 🔹 Step 3: Setup DHT11 sensor
sensor = dht.DHT11(Pin(15))   # DHT11 data pin → GPIO15

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("🔌 Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("... still trying")
    print("✅ Connected:", wlan.ifconfig())

def ask_ai(temperature, humidity):
    try:
        # Create JSON payload
        payload = {"temperature": temperature, "humidity": humidity}

        # Send POST to Lambda
        response = urequests.post(
            LAMBDA_URL,
            headers={"Content-Type": "application/json"},
            data=ujson.dumps(payload)
        )

        # Parse response from Lambda
        result = response.json()
        response.close()

        return result.get("answer", "⚠️ No 'answer' in response")

    except Exception as e:
        return "❌ Error: " + str(e)

def main():
    connect_wifi()

    while True:
        try:
            # Read sensor
            sensor.measure()
            t = sensor.temperature()
            h = sensor.humidity()

            print("🌡 Temperature:", t, "°C")
            print("💧 Humidity:", h, "%")

            # Ask AI (via Lambda)
            ai_reply = ask_ai(t, h)
            print("AI says:", ai_reply)

        except Exception as e:
            print("❌ Sensor or request error:", e)

        # Wait 10 seconds before next reading
        time.sleep(10)

main()
