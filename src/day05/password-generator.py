#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
numberOfLetters= int(input("How many letters would you like in your password?\n")) 
numberOfSymbols = int(input(f"How many symbols would you like?\n"))
numberOfNumbers = int(input(f"How many numbers would you like?\n"))

# Order not randomised
password = ""

for letter in range(0, numberOfLetters):
  password += random.choice(letters)

for symbol in range(0, numberOfSymbols):
  password += random.choice(symbols)

for number in range(0, numberOfNumbers):
  password += random.choice(numbers)

print(f"Your password is: {password}")


#Order of characters are randomised:
passwordList = []

for letter in range(0, numberOfLetters):
  passwordList.append( random.choice(letters))

for symbol in range(0, numberOfSymbols):
  passwordList.append(random.choice(symbols))

for number in range(0, numberOfNumbers):
  passwordList.append(random.choice(numbers))

random.shuffle(passwordList)

password = ""
for char in passwordList:
  password += char

print(f"Your password is: {password}")