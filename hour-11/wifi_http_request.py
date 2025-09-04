import network
import time
import urequests

# WiFi credentials - replace with your actual WiFi details
ssid = "my-wifi"
password = "Password1"

def connect():
    """Connect the Pico to WiFi network"""
    # Set up wireless module instance, turn on the wireless hardware
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connection and show status
    while wlan.isconnected() == False:
        print("Connecting, please wait...")
        time.sleep(1)
    
    # Print IP address once connected
    print("Connected! IP = ", wlan.ifconfig()[0])

# Main program execution
try:
    # Connect to WiFi
    connect()
    
    # Define the AWS Lambda URL to query
    site = "https://3uemzm5mum3l6mjdt7iovq7h3y0nnseo.lambda-url.ap-south-1.on.aws/"
    print("Querying: ", site)
    
    # Make HTTP request to the site
    r = urequests.get(site)
    
    # Print the response
    print("Response:", r.json())
    
    # Close the connection
    r.close()
    
except OSError as e:
    # Handle connection errors
    print("Error: connection failed -", e)
    if 'r' in locals():
        r.close()
    print("Connection closed")