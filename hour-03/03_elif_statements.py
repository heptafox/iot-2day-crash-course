# Hour 03: Elif Statements
# Elif means "else if" - it checks more options

# Example 1: What to wear
temperature = 25
if temperature > 30:
    print("Wear shorts!")
elif temperature > 20:
    print("Wear a t-shirt!")
else:
    print("Wear a jacket!")

# Example 2: Traffic light
color = "red"
if color == "green":
    print("Go!")
elif color == "yellow":
    print("Wait!")
else:
    print("Stop!")

# Example 3: How old are you?
age = 15
if age < 10:
    print("You're a kid!")
elif age < 18:
    print("You're a teenager!")
else:
    print("You're grown up!")