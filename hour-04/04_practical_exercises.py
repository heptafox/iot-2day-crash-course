# Hour 04 - Simple Practice (Easy Version)
# Fun exercises with loops

print("LOOP PRACTICE - Fun Examples")
print("=" * 30)

# Exercise 1: Count your age in dog years
print("\n1. Dog years calculator:")
for age in range(1, 6):
    dog_years = age * 7
    print("Age", age, "= Dog age", dog_years)

# Exercise 2: Shopping list
print("\n2. My shopping list:")
items = ["milk", "bread", "eggs", "apples"]
for item in items:
    print("Buy", item)

# Exercise 3: Counting money
print("\n3. Counting coins:")
coins = 0
while coins < 10:
    coins = coins + 1
    print("I have", coins, "coins")

# Exercise 4: Simple times table
print("\n4. Times table for 3:")
for number in range(1, 6):
    answer = 3 * number
    print("3 x", number, "=", answer)

# Exercise 5: Favorite colors
print("\n5. My favorite colors:")
colors = ["red", "blue", "green", "yellow"]
count = 1
for color in colors:
    print("Color", count, "is", color)
    count = count + 1

# Exercise 6: Count down to zero
print("\n6. Rocket countdown:")
countdown = 5
while countdown > 0:
    print(countdown, "...")
    countdown = countdown - 1
print("Blast off!")

print("\nGreat job! You learned about loops!")