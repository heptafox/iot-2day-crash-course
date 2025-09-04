# Simple DHT11 Web Server - Beginner Friendly Version
# Basic REST endpoints for temperature and humidity

import network
import socket
import dht
from machine import Pin
import time

# WiFi Settings - CHANGE THESE!
WIFI_SSID = "your-wifi-name"
WIFI_PASSWORD = "your-password"

# DHT11 sensor on pin 15
sensor = dht.DHT11(Pin(15))

def connect_to_wifi():
    """Connect to WiFi and return IP address"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("Still connecting...")
    
    ip = wlan.ifconfig()[0]
    print(f"Connected! Your Pico's IP: {ip}")
    return ip

def get_sensor_data():
    """Read temperature and humidity from DHT11"""
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        return temp, humidity
    except:
        return None, None

def create_web_page(temp, humidity):
    """Create simple HTML page showing sensor data"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DHT11 Sensor</title>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>DHT11 Sensor Data</h1>
        <h2>Temperature: {temp}°C</h2>
        <h2>Humidity: {humidity}%</h2>
        <p>Page refreshes every 5 seconds</p>
        <hr>
        <p>API Endpoints:</p>
        <ul>
            <li><a href="/temperature">/temperature</a> - Get temperature only</li>
            <li><a href="/humidity">/humidity</a> - Get humidity only</li>
        </ul>
    </body>
    </html>
    """
    return html

# Main program starts here
print("Starting DHT11 Web Server...")

# Connect to WiFi
ip_address = connect_to_wifi()

# Create web server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))  # Port 80 for web server
server_socket.listen(5)

print(f"Web server running at: http://{ip_address}")
print("Available URLs:")
print(f"  http://{ip_address}/           - Main page")
print(f"  http://{ip_address}/temperature - Temperature only")
print(f"  http://{ip_address}/humidity    - Humidity only")
print("\nWaiting for connections...")

while True:
    try:
        # Wait for someone to connect
        client_socket, client_address = server_socket.accept()
        print(f"Connection from: {client_address}")
        
        # Get the request
        request = client_socket.recv(1024).decode()
        
        # Find what page they want
        if 'GET /' in request:
            if 'GET /temperature' in request:
                # Just temperature
                temp, _ = get_sensor_data()
                response = f"Temperature: {temp}°C"
                
            elif 'GET /humidity' in request:
                # Just humidity  
                _, humidity = get_sensor_data()
                response = f"Humidity: {humidity}%"
                
            else:
                # Main page with both
                temp, humidity = get_sensor_data()
                response = create_web_page(temp, humidity)
        
        # Send response back
        client_socket.send('HTTP/1.1 200 OK\n')
        client_socket.send('Content-Type: text/html\n')
        client_socket.send('Connection: close\n\n')
        client_socket.sendall(response)
        client_socket.close()
        
    except KeyboardInterrupt:
        print("\nStopping server...")
        break
    except Exception as e:
        print(f"Error: {e}")

server_socket.close()
print("Server stopped.")