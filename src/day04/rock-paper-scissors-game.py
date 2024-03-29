import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissor
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computerChoice = random.randint(0, 2)

print(f"Computer chose {computerChoice}")

if userChoice >= 3 or userChoice < 0:
  print("You typed an invalid number, you lose!")
elif userChoice == 0 and computerChoice == 2:
  print("You win!")
elif computerChoice == 0 and userChoice == 2:
  print("You lose!")
elif computerChoice > userChoice:
  print("You lose!")
elif userChoice > computerChoice:
  print("You win!")
elif computerChoice == userChoice:
  print("It's a draw!")