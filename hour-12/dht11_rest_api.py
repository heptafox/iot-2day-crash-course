# DHT11 REST API Server - Simple Web Server for Temperature & Humidity
# Creates REST endpoints to read DHT11 sensor data over WiFi

import network
import socket
import time
import dht
from machine import Pin
import json

# WiFi credentials - replace with your actual WiFi details
SSID = "your-wifi-name"
PASSWORD = "your-wifi-password"

# DHT11 sensor setup on pin 15
sensor = dht.DHT11(Pin(15))

# Global variables to store latest readings
latest_temperature = 0
latest_humidity = 0

def connect_wifi():
    """Connect the Pico W to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    
    print(f"\nConnected! IP address: {wlan.ifconfig()[0]}")
    return wlan.ifconfig()[0]

def read_sensor():
    """Read DHT11 sensor and update global variables"""
    global latest_temperature, latest_humidity
    try:
        sensor.measure()
        latest_temperature = sensor.temperature()
        latest_humidity = sensor.humidity()
        print(f"Sensor reading: {latest_temperature}°C, {latest_humidity}%")
    except OSError:
        print("Sensor read failed")

def create_response(status, content_type, body):
    """Create HTTP response"""
    response = f"HTTP/1.1 {status}\r\n"
    response += f"Content-Type: {content_type}\r\n"
    response += "Access-Control-Allow-Origin: *\r\n"
    response += f"Content-Length: {len(body)}\r\n"
    response += "\r\n"
    response += body
    return response

def handle_request(request):
    """Handle incoming HTTP requests"""
    try:
        # Parse the request line
        request_line = request.split('\r\n')[0]
        method, path, _ = request_line.split(' ')
        
        if method == 'GET':
            if path == '/temperature':
                # Return temperature as JSON
                data = {"temperature": latest_temperature, "unit": "celsius"}
                return create_response("200 OK", "application/json", json.dumps(data))
            
            elif path == '/humidity':
                # Return humidity as JSON
                data = {"humidity": latest_humidity, "unit": "percent"}
                return create_response("200 OK", "application/json", json.dumps(data))
            
            elif path == '/':
                # Return simple HTML page with both readings
                html = f"""
                <html>
                <head><title>DHT11 Sensor</title></head>
                <body>
                <h1>DHT11 Sensor Readings</h1>
                <p>Temperature: {latest_temperature}°C</p>
                <p>Humidity: {latest_humidity}%</p>
                <p><a href="/temperature">Temperature JSON</a></p>
                <p><a href="/humidity">Humidity JSON</a></p>
                </body>
                </html>
                """
                return create_response("200 OK", "text/html", html)
        
        # 404 for unknown paths
        return create_response("404 Not Found", "text/plain", "Not Found")
    
    except Exception as e:
        print(f"Request handling error: {e}")
        return create_response("500 Internal Server Error", "text/plain", "Server Error")

def start_server():
    """Start the web server"""
    # Create socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    
    print("Web server started on port 80")
    print("Available endpoints:")
    print("  http://[IP_ADDRESS]/          - HTML page with readings")
    print("  http://[IP_ADDRESS]/temperature - Temperature JSON")
    print("  http://[IP_ADDRESS]/humidity    - Humidity JSON")
    
    return s

# Main program
def main():
    # Connect to WiFi
    ip = connect_wifi()
    
    # Start web server
    server = start_server()
    
    # Initial sensor reading
    read_sensor()
    
    print(f"\nServer running at http://{ip}")
    print("Reading sensor every 10 seconds...")
    
    last_sensor_read = time.time()
    
    while True:
        try:
            # Read sensor every 10 seconds
            if time.time() - last_sensor_read > 10:
                read_sensor()
                last_sensor_read = time.time()
            
            # Check for incoming connections (non-blocking)
            server.settimeout(0.1)
            try:
                conn, addr = server.accept()
                print(f"Connection from {addr}")
                
                # Receive request
                request = conn.recv(1024).decode('utf-8')
                
                # Handle request and send response
                response = handle_request(request)
                conn.send(response.encode('utf-8'))
                conn.close()
                
            except OSError:
                # No connection available, continue
                pass
                
        except KeyboardInterrupt:
            print("\nShutting down server...")
            server.close()
            break
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    main()