# Hour 06 - Random Library (Simple Version)
# The random library makes random numbers and choices

print("RANDOM LIBRARY - Easy Examples")
print("=" * 34)

# Import the random library
import random

# Example 1: Random numbers between 1 and 10
print("\n1. Random numbers from 1 to 10:")
print("Random number:", random.randint(1, 10))
print("Random number:", random.randint(1, 10))
print("Random number:", random.randint(1, 10))

# Example 2: Random choice from a list
print("\n2. Random choice from a list:")
colors = ["red", "blue", "green", "yellow", "purple"]
print("Random color:", random.choice(colors))
print("Random color:", random.choice(colors))
print("Random color:", random.choice(colors))

# Example 3: Random animals
print("\n3. Random animals:")
animals = ["cat", "dog", "bird", "fish", "rabbit"]
print("Random animal:", random.choice(animals))
print("Random animal:", random.choice(animals))

# Example 4: Dice roll
print("\n4. Rolling a dice:")
for i in range(5):
    dice = random.randint(1, 6)
    print("Dice roll", i+1, ":", dice)

# Example 5: Random yes or no
print("\n5. Random yes or no:")
answers = ["yes", "no"]
for i in range(4):
    answer = random.choice(answers)
    print("Answer", i+1, ":", answer)

# Example 6: Coin flip
print("\n6. Coin flip:")
coin = ["heads", "tails"]
for i in range(3):
    flip = random.choice(coin)
    print("Flip", i+1, ":", flip)

print("\nRandom makes programs fun and unpredictable!")