# Hour 05 - Practice Exercises (Simple Version)
# Fun practice with parameters, return values, and global variables

print("PRACTICE EXERCISES - Fun Examples")
print("=" * 38)

# Global variables for our exercises
bank_balance = 100
pizza_slices = 8

# Exercise 1: Calculator functions
print("\n1. Simple calculator:")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 x 7 =", multiply(6, 7))

# Exercise 2: Name functions
print("\n2. Name functions:")
def make_full_name(first, last):
    return first + " " + last

def greet_person(name):
    return "Nice to meet you, " + name

full_name = make_full_name("John", "Smith")
greeting = greet_person(full_name)
print(full_name)
print(greeting)

# Exercise 3: Bank account (using global variable)
print("\n3. Bank account:")
def check_balance():
    print("Your balance is $" + str(bank_balance))

def deposit(amount):
    global bank_balance
    bank_balance = bank_balance + amount
    print("Deposited $" + str(amount))
    check_balance()

def withdraw(amount):
    global bank_balance
    if amount <= bank_balance:
        bank_balance = bank_balance - amount
        print("Withdrew $" + str(amount))
    else:
        print("Not enough money!")
    check_balance()

check_balance()
deposit(50)
withdraw(30)
withdraw(200)  # This should fail

# Exercise 4: Pizza party (using global variable)
print("\n4. Pizza party:")
def eat_pizza(person_name, slices_eaten):
    global pizza_slices
    if slices_eaten <= pizza_slices:
        pizza_slices = pizza_slices - slices_eaten
        print(person_name, "ate", slices_eaten, "slices")
        print("Slices left:", pizza_slices)
    else:
        print("Not enough pizza left!")

def order_more_pizza(new_slices):
    global pizza_slices
    pizza_slices = pizza_slices + new_slices
    print("Ordered", new_slices, "more slices")
    print("Total slices now:", pizza_slices)

print("Starting with", pizza_slices, "pizza slices")
eat_pizza("Mike", 2)
eat_pizza("Lisa", 3)
eat_pizza("Tom", 5)  # This should fail
order_more_pizza(8)
eat_pizza("Tom", 5)  # Now this should work

# Exercise 5: Temperature converter
print("\n5. Temperature converter:")
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(str(temp_c) + "°C = " + str(temp_f) + "°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(str(temp_f) + "°F = " + str(temp_c) + "°C")

print("\nGreat job! You learned about functions!")