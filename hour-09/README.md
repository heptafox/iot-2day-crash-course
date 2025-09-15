## Hour 09: Wi‑Fi, HTTP, and Cloud APIs (Pico W + MicroPython)

Connect the Pico W to Wi‑Fi, call HTTP endpoints, do a simple speed test, and control an LED from cloud weather data.

### Prerequisites
- Pico W with MicroPython firmware that supports `network`.
- `urequests` module available on the board (copy `urequests.py` if needed).
- Update SSID/password in the scripts before running.

### 01_wifi_http_request.py
- **Goal**: Connect to Wi‑Fi and send a GET request to an AWS Lambda Function URL, passing a `name` query parameter.
- **How it works**:
  - Connects using `network.WLAN(network.STA_IF)` and waits for `isconnected()`.
  - Builds `https://...lambda-url.../?name=<your_name>` and calls `urequests.get()`.
  - Prints the JSON response and closes the response object.
- **Configure**:
  - Set `ssid` and `password`.
  - Optionally change `my_name` and the Lambda `site` URL.

### 02_internet_speed_test.py
- **Goal**: Crude download/upload speed check over Wi‑Fi.
- **How it works**:
  - Connects to Wi‑Fi, then:
    - Download: GET `http://speedtest.tele2.net/1MB.zip`, measures time, computes KB/s.
    - Upload: POST 1 KB to `http://httpbin.org/post`, measures time, computes KB/s.
- **Notes**:
  - Results are rough and depend on server reachability and network quality.
  - Large downloads can be slow or memory‑heavy on microcontrollers; keep sizes small.

### 03_weather_led_control.py
- **Goal**: Query a weather API (AWS Lambda Function URL) for a city and control an LED based on temperature.
- **How it works**:
  - Connects to Wi‑Fi, calls `BASE_URL` with `?city=<CITY>`.
  - Parses JSON; if `temperature > 30°C` turns LED ON, else OFF.
  - Handles various response shapes (dict with error, dict with fields, or list fallback).
- **Configure**:
  - Set `ssid`, `password`, `BASE_URL`, and `CITY`.
  - LED is `Pin(2, Pin.OUT)` by default (external LED). To use onboard LED on Pico W, set `Pin("LED", Pin.OUT)` or `Pin(25, Pin.OUT)` depending on board/port.
- **Wiring (if using external LED)**:
  - `GPIO2` → resistor (220–330Ω) → LED anode (+)
  - LED cathode (−) → GND

### info.txt (AWS Lambda Function URL setup)
- Contains example AWS CLI commands to:
  - Create a Function URL for a Lambda (`--auth-type NONE`) with permissive CORS.
  - Add public invoke permission for the Function URL.
- The file also lists example Function URLs used by the scripts.
- Security note: Public Function URLs with `NONE` auth are world‑readable; protect or restrict as needed.

### Running and stopping
- Save scripts to the board and run from Thonny/REPL.
- Press Ctrl+C in the REPL to stop.
- If connection fails, verify SSID/password, check 2.4 GHz availability, and ensure `urequests` is present.


