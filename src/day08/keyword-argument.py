# function with parameters
def greetings(name, greetWord):
  print(f"{greetWord} {name}")

# positional arguments
greetings("Aduvai", "welcome")

# keyword arguments
greetings(name="Aduvai", greetWord="Good morning")
greetings(greetWord="Good morning", name="Aduvai")