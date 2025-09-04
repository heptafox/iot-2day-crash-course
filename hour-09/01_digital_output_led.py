# Simple LED Blink - Beginner Program
# This makes the onboard LED blink on and off

from machine import Pin
import time

led = Pin("LED", Pin.OUT) # Set up the onboard LED (can replace "LED" with a pin GPIO number)

#led = Pin(25, Pin.OUT) # Set up the LED (it's on pin 25)


# Blink forever
while True:
    led.on()        # Turn LED ON (3.3V)
    time.sleep(2)   # Wait 1 second
    led.off()       # Turn LED OFF (0V)
    time.sleep(2)   # Wait 1 second