enemies = 1

def increseEnemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increseEnemies()
print(f"enemies outside function: {enemies}")

# Local scope
def darkPoision():
  poisionStrength = 2
  print(poisionStrength)

darkPoision()

# poisionStrength variable is local to the function
# print(poisionStrength)

# Global scope
playerHealth = 10

def drinkDarkPoision():
  # can access global soce variables
  print(playerHealth)

drinkDarkPoision()
print(playerHealth)