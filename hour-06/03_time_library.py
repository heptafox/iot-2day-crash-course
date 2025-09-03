# Hour 06 - Time Library (Simple Version)
# The time library helps with delays and time

print("TIME LIBRARY - Easy Examples")
print("=" * 31)

# Import the time library
import time

# Example 1: Simple countdown with delays
print("\n1. Countdown with delays:")
print("Starting countdown...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # Wait 1 second
print("Go!")

# Example 2: Show current time
print("\n2. Current time:")
current_time = time.time()
print("Time since 1970 (seconds):", current_time)

# Example 3: Readable time
print("\n3. Readable time:")
readable_time = time.ctime()
print("Current date and time:", readable_time)

# Example 4: Stopwatch simulation
print("\n4. Simple stopwatch (3 seconds):")
print("Starting...")
start_time = time.time()
time.sleep(3)  # Wait 3 seconds
end_time = time.time()
elapsed = end_time - start_time
print("Elapsed time:", elapsed, "seconds")

# Example 5: Blinking message
print("\n5. Blinking message:")
for i in range(3):
    print("HELLO!")
    time.sleep(0.5)  # Wait half a second
    print("     ")  # Spaces to "clear" the message
    time.sleep(0.5)

print("\n6. Loading simulation:")
print("Loading", end="")
for i in range(5):
    print(".", end="")
    time.sleep(0.5)
print(" Done!")

print("\nTime library helps control when things happen!")