# For Loops - Beginner Examples
# For loops repeat code a specific number of times

print("FOR LOOPS - Easy Examples")
print("=" * 30)

# Example 1: Count to 5 (starts from 0)
print("\n1. Counting to 5:")
for i in range(5):
    print(i)

# Example 2: Say hello 3 times
print("\n2. Say hello 3 times:")
for i in range(3):
    print("Hello!")

# Example 3: Print numbers 1 to 5
print("\n3. Numbers 1 to 5:")
for i in range(1, 6):
    print(i)

# Example 4: Simple multiplication table
print("\n4. Multiplication table for 2:")
for i in range(1, 6):
    print("2 x", i, "=", 2 * i)

# Example 5: Loop through a list
print("\n5. My favorite fruits:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)
