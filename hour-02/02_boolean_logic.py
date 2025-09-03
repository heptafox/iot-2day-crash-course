# Hour 2: Boolean Logic

print("Boolean Logic")
print("=============")

# Simple conditions
sunny = True
cold = False

print(f"sunny = {sunny}")
print(f"cold = {cold}")
print()

# AND - both must be true
print("AND operator:")
print(f"sunny and cold: {sunny and cold}")      # True and False = False
print(f"sunny and not cold: {sunny and not cold}")  # True and True = True
print()

# OR - at least one must be true
print("OR operator:")
print(f"sunny or cold: {sunny or cold}")        # True or False = True
print()

# NOT - reverses True/False
print("NOT operator:")
print(f"not sunny: {not sunny}")               # not True = False
print(f"not cold: {not cold}")                 # not False = True