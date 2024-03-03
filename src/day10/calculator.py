import importlib
calculatorLogo = importlib.import_module("calculator-logo")

# Calculator
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

print(calculatorLogo.logo)
num1 = float(input("What's the first number?: "))
num2 = float(input("What's the second number?: "))
for symbol in operations:
  print(symbol)
operationSymbol = input("Pick an operation from the line above: ")

answer = operations[operationSymbol](num1, num2)

print(f"{num1} {operationSymbol} {num2} = {answer}")