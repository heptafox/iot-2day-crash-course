# Simple Button Reader - Beginner Program
# Connect a button between pin 14 and GND

from machine import Pin
import time

# Set up button (pin 14) and LED (pin 25)
button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

# Check button forever
while True:
    if button.value() == 0:    # Button pressed (reads 0V)
        led.on()               # Turn LED on
        print("Button pressed - LED ON")
    else:                      # Button not pressed (reads 3.3V)
        led.off()              # Turn LED off
        print("Button released - LED OFF")
    
    time.sleep(0.1)            # Small delay