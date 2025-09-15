import network
import time
import urequests

# WiFi credentials - put your WiFi name and password
SSID = "nothing_phone"
PASSWORD = "abny6663"


def connect_wifi():
    """Connect to WiFi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("Still connecting...")

    print("Connected! IP address:", wlan.ifconfig()[0])


def test_download():
    """Check download speed (very simple test)"""
    url = "http://speedtest.tele2.net/1MB.zip"
    start_time = time.time()
    r = urequests.get(url)
    data = r.content  # download full file
    r.close()
    end_time = time.time()

    size_kb = len(data) / 1024
    seconds = end_time - start_time
    speed_kbps = size_kb / seconds
    print("Download speed: {:.2f} KB/s".format(speed_kbps))


def test_upload():
    """Check upload speed (very simple test)"""
    url = "http://httpbin.org/post"
    data = b"x" * 1024  # 1 KB data
    start_time = time.time()
    r = urequests.post(url, data=data)
    r.close()
    end_time = time.time()

    seconds = end_time - start_time
    speed_kbps = len(data) / 1024 / seconds
    print("Upload speed: {:.2f} KB/s".format(speed_kbps))


def main():
    connect_wifi()
    test_download()
    test_upload()
    print("Done.")


main()
