import random
from hangmanStages import stages
from wordList import word_list


print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
      ''')


# user lives
lives = 6

# randomly select a word
# chosenWord = random.choice(word_list)
chosenWord = "banana"

display = []
for _ in range(len(chosenWord)):
  display += "_"


endOfGame = False
while not endOfGame:
  # guess a letter
  userGuess = input("Guess a letter: ").lower()

  if userGuess in display:
    print(f"You've already guessed {userGuess}")

   #Check guessed letter
  for index in range(len(chosenWord)):
    letter = chosenWord[index]
    if letter == userGuess:
      display[index] = letter

  # check wrong guess
  if userGuess not in chosenWord:
    print(f"You guessed {userGuess}, tht's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      endOfGame = True
      print("You lose")
    print(stages[lives])

  print(f"{' '.join(display)}")

  # win the game
  if "_" not in display:
    end_of_game = True
    print("You win.")


