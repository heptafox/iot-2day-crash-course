import network
import time
import urequests

# WiFi credentials - replace with your actual WiFi details
ssid = "my_wifi"
password = "Password1"

def connect():
    """Connect the Pico to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print("Connecting, please wait...")
        time.sleep(1)
    
    print("Connected! IP = ", wlan.ifconfig()[0])

# Main program
try:
    connect()
    
    # Lambda URL
    site = "https://3uemzm5mum3l6mjdt7iovq7h3y0nnseo1.lambda-url.ap-south-1.on.aws/"
    
    # Add name as query parameter
    my_name = "Boobathi"
    url_with_name = f"{site}?name={my_name}"
    
    print("Querying:", url_with_name)
    
    # GET request with name
    r = urequests.get(url_with_name)
    
    print("Response:", r.json())
    r.close()
    
except OSError as e:
    print("Error: connection failed -", e)
    if 'r' in locals():
        r.close()
    print("Connection closed")


#https://3uemzm5mum3l6mjdt7iovq7h3y0nnseo1.lambda-url.ap-south-1.on.aws/?name=Boobathi