# Hour 06 - Different Ways to Import (Simple Version)
# There are different ways to import libraries

print("DIFFERENT WAYS TO IMPORT")
print("=" * 28)

# Way 1: Import the whole library
print("\n1. Import whole library:")
import math
print("Using math.sqrt(16):", math.sqrt(16))

# Way 2: Import specific functions
print("\n2. Import specific functions:")
from math import sqrt, pi
print("Using sqrt(25):", sqrt(25))
print("Using pi:", pi)

# Way 3: Import with a shorter name
print("\n3. Import with shorter name:")
import random as r
print("Random number:", r.randint(1, 100))

# Way 4: Import everything (not recommended but simple)
print("\n4. Import everything from time:")
from time import sleep, ctime
print("Current time:", ctime())
print("Sleeping for 1 second...")
sleep(1)
print("Done sleeping!")

# Example: Using different import styles together
print("\n5. Using different styles together:")

# Regular import
import math
circle_area = math.pi * 5 * 5
print("Circle area (radius 5):", circle_area)

# Specific import
from random import choice
pets = ["cat", "dog", "bird"]
random_pet = choice(pets)
print("Random pet:", random_pet)

# Import with alias
import time as t
print("Waiting 1 second...")
t.sleep(1)
print("Done!")

print("\nChoose the import style that makes your code easy to read!")