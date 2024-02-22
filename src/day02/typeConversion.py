numOfChar = len(input("What is your name? "))

# Type Error
# print("Your name has " + numOfChar + " Characters.")
# TypeError: can only concatenate str (not "int") to str

# Type Checking
print(type(numOfChar))
print(type("Hello"))

# Type Conversion
print(str(123))
print(float(123))
print(int("123"))
print("Your name has " + str(numOfChar) + " Characters.")