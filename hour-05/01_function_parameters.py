# Hour 05 - Function Parameters (Simple Version)
# Functions can take inputs called parameters

print("FUNCTION PARAMETERS - Easy Examples")
print("=" * 40)

# Example 1: Function with one parameter
print("\n1. Function that says hello to someone:")
def say_hello(name):
    print("Hello", name)

say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")

# Example 2: Function with two parameters
print("\n2. Function that adds two numbers:")
def add_numbers(first, second):
    result = first + second
    print(first, "+", second, "=", result)

add_numbers(5, 3)
add_numbers(10, 7)
add_numbers(2, 8)

# Example 3: Function that makes a sentence
print("\n3. Function that makes sentences:")
def make_sentence(animal, sound):
    print("The", animal, "says", sound)

make_sentence("cat", "meow")
make_sentence("dog", "woof")
make_sentence("cow", "moo")

# Example 4: Function with three parameters
print("\n4. Function that calculates age:")
def show_age(name, birth_year, current_year):
    age = current_year - birth_year
    print(name, "is", age, "years old")

show_age("Emma", 2010, 2024)
show_age("Jake", 2005, 2024)

# Example 5: Function that repeats text
print("\n5. Function that repeats words:")
def repeat_word(word, times):
    for i in range(times):
        print(word)

print("Repeating 'Python' 3 times:")
repeat_word("Python", 3)

print("\nRepeating 'Fun' 2 times:")
repeat_word("Fun", 2)