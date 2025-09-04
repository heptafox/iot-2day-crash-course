# Hour 12: DHT11 REST API Server

This folder contains programs that create a web server on your Pico W to serve DHT11 sensor data via REST endpoints.

## Files

### `simple_dht11_server.py` - Beginner Version
- Easy to understand and modify
- Creates basic web server with DHT11 readings
- Auto-refreshing web page

### `dht11_rest_api.py` - Advanced Version  
- Full REST API with JSON responses
- Better error handling
- More professional structure

## Hardware Setup

**DHT11 Wiring:**
- DHT11 VCC → 3.3V on Pico W
- DHT11 GND → GND on Pico W  
- DHT11 Data → GPIO pin 15

## How to Use

1. **Update WiFi credentials** in the code:
   ```python
   WIFI_SSID = "your-wifi-name"
   WIFI_PASSWORD = "your-password"
   ```

2. **Upload and run** the program on your Pico W

3. **Find your Pico's IP address** in the console output

4. **Access the endpoints:**
   - `http://[IP_ADDRESS]/` - Main page with readings
   - `http://[IP_ADDRESS]/temperature` - Temperature only
   - `http://[IP_ADDRESS]/humidity` - Humidity only

## Example Usage

Once running, you can:
- Open the IP address in your browser to see live readings
- Use curl or other tools to get data:
  ```bash
  curl http://192.168.1.100/temperature
  curl http://192.168.1.100/humidity
  ```

## Troubleshooting

- Make sure WiFi credentials are correct
- Check DHT11 wiring connections
- Ensure Pico W and your device are on same network
- Try accessing from phone browser if computer doesn't work