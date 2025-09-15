# Simple Button Reader
# Read button state and display on console

from machine import Pin
import time

# Set up button on pin 15 with internal pull-up
button = Pin(15, Pin.IN, Pin.PULL_UP)

print("Button Reader Started")
print("Press and release the button to see the readings")

# Main loop
while True:
    if button.value() == 0:    # Button pressed (active low)
        print("Button pressed")
    else:                      # Button released
        print("Button released")
    
    time.sleep(0.2)            # Small delay to prevent excessive printing

#OK