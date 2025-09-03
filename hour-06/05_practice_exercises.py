# Hour 06 - Practice with Libraries (Simple Version)
# Fun exercises using different libraries

print("LIBRARY PRACTICE - Fun Examples")
print("=" * 35)

# Import all the libraries we need
import math
import random
import time

# Exercise 1: Random math quiz
print("\n1. Random math quiz:")
for i in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    print("Question", i+1, ":", num1, "+", num2, "= ?")
    print("Answer:", correct_answer)
    time.sleep(1)  # Pause between questions

# Exercise 2: Circle calculator
print("\n2. Circle calculator:")
radiuses = [3, 5, 7, 10]
for radius in radiuses:
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print("Radius", radius, ":")
    print("  Area:", round(area, 2))
    print("  Circumference:", round(circumference, 2))

# Exercise 3: Random story generator
print("\n3. Random story generator:")
names = ["Alice", "Bob", "Charlie", "Diana"]
animals = ["cat", "dog", "bird", "fish"]
colors = ["red", "blue", "green", "yellow"]
actions = ["runs", "jumps", "sleeps", "plays"]

for i in range(3):
    name = random.choice(names)
    animal = random.choice(animals)
    color = random.choice(colors)
    action = random.choice(actions)
    
    story = name + " has a " + color + " " + animal + " that " + action
    print("Story", i+1, ":", story)

# Exercise 4: Dice game
print("\n4. Simple dice game:")
print("Rolling two dice 5 times:")
for i in range(5):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Roll", i+1, ":", dice1, "+", dice2, "=", total)
    
    if total == 7:
        print("  Lucky seven!")
    elif total == 12:
        print("  Double six!")

# Exercise 5: Timer with random messages
print("\n5. Timer with random messages:")
messages = ["Keep going!", "You're doing great!", "Almost there!", "Nice work!"]

print("5-second timer with random encouragement:")
for i in range(5, 0, -1):
    print("Time left:", i)
    if i <= 3:  # Show message in last 3 seconds
        message = random.choice(messages)
        print("  " + message)
    time.sleep(1)
print("Time's up!")

# Exercise 6: Square root guessing game
print("\n6. Square root guessing game:")
numbers = [16, 25, 36, 49, 64]
for number in numbers:
    correct_answer = math.sqrt(number)
    print("What's the square root of", number, "?")
    print("Answer:", int(correct_answer))

print("\nGreat job using libraries to make cool programs!")