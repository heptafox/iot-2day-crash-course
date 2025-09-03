# Hour 05 - Return Values (Simple Version)
# Functions can send back answers using return

print("RETURN VALUES - Easy Examples")
print("=" * 35)

# Example 1: Function that returns a number
print("\n1. Function that doubles a number:")
def double_number(number):
    result = number * 2
    return result

answer = double_number(5)
print("Double of 5 is", answer)

answer = double_number(8)
print("Double of 8 is", answer)

# Example 2: Function that returns text
print("\n2. Function that makes a greeting:")
def make_greeting(name):
    greeting = "Hi there, " + name + "!"
    return greeting

message = make_greeting("Sarah")
print(message)

message = make_greeting("Tom")
print(message)

# Example 3: Function that calculates and returns
print("\n3. Function that calculates area:")
def calculate_area(length, width):
    area = length * width
    return area

room_area = calculate_area(10, 12)
print("Room area is", room_area, "square feet")

garden_area = calculate_area(5, 8)
print("Garden area is", garden_area, "square feet")

# Example 4: Function that checks something
print("\n4. Function that checks if number is big:")
def is_big_number(number):
    if number > 100:
        return "Yes, that's big!"
    else:
        return "No, that's small"

result = is_big_number(150)
print("Is 150 big?", result)

result = is_big_number(50)
print("Is 50 big?", result)

# Example 5: Using return value in calculations
print("\n5. Using returned values:")
def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

sum_result = add_two_numbers(3, 4)
multiply_result = multiply_two_numbers(5, 6)

print("3 + 4 =", sum_result)
print("5 x 6 =", multiply_result)
print("Sum + Product =", sum_result + multiply_result)