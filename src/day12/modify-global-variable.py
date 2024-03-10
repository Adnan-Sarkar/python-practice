enemies = 2

def increaseEnemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increaseEnemies()
print(f"enemies outside function: {enemies}")