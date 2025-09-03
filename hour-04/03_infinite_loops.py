# Hour 04 - Infinite Loops (Simple Version)
# IMPORTANT: Infinite loops run forever unless you stop them!

print("INFINITE LOOPS - Be Careful!")
print("=" * 30)

# Example 1: Safe infinite loop with break
print("\n1. Infinite loop that stops after 3 times:")
count = 0
while True:  # This means "keep going forever"
    print("This is loop number", count + 1)
    count = count + 1
    
    # ALWAYS have a way to stop!
    if count == 3:
        print("Stopping the loop now")
        break  # This stops the infinite loop

# Example 2: Simple menu that keeps asking
print("\n2. Simple menu (pretend game):")
choices = ["1", "2", "3"]  # Pretend user picks these
choice_number = 0

while True:
    print("\nWhat do you want to do?")
    print("1. Play game")
    print("2. See score") 
    print("3. Quit")
    
    # Pretend user picks something
    if choice_number < len(choices):
        choice = choices[choice_number]
        print("You picked:", choice)
        choice_number = choice_number + 1
    else:
        choice = "3"  # Force quit
    
    if choice == "1":
        print("Playing game...")
    elif choice == "2":
        print("Your score is 100!")
    elif choice == "3":
        print("Bye!")
        break  # Stop the infinite loop
    else:
        print("I don't understand")

print("\n⚠️ DANGER WARNING:")
print("Never write 'while True:' without 'break'!")
print("Your program will run forever and freeze!")
print("Always have a way to stop the loop!")

# DON'T DO THIS (it's commented out so it won't run):
# while True:
#     print("This would never stop!")
#     # No break = BAD!