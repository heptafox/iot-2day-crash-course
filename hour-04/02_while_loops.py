# Hour 04 - While Loops (Simple Version)
# While loops keep running while something is true

print("WHILE LOOPS - Easy Examples")
print("=" * 30)

# Example 1: Simple countdown
print("\n1. Countdown from 5:")
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Done!")

# Example 2: Keep adding until we reach 10
print("\n2. Adding numbers until we reach 10:")
total = 0
number = 1
while total < 10:
    print("Adding", number, "Total is now", total + number)
    total = total + number
    number = number + 1

# Example 3: Simple password check
print("\n3. Password check (pretend game):")
password = "secret"
guess = "wrong"
tries = 0

# We'll pretend the user tries these passwords
guesses = ["hello", "password", "secret"]

while guess != password and tries < 3:
    guess = guesses[tries]  # Pretend user typed this
    print("You typed:", guess)
    
    if guess == password:
        print("Correct! Welcome!")
    else:
        print("Wrong password, try again")
    
    tries = tries + 1

# Example 4: Keep going until we find the right answer
print("\n4. Looking for the number 7:")
numbers = [1, 3, 5, 7, 9]
position = 0

while numbers[position] != 7:
    print("This number is", numbers[position], "- not 7")
    position = position + 1

print("Found 7!")