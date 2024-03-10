import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def checkResult(guess, answer, turns):
  """
  Checks answer against guess. Returns the number of turns remaining
  """
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer wa {answer}.")

def setDifficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty.lower() == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  

def startGame():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")

  answer = random.randint(0, 100)
  turns = setDifficulty()
  guess = -1

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = checkResult(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

startGame()