import random
import gameLogo

def dealCard():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculateScore(cards):
  """
  Take a list of cards and return the score of calculated from the cards
  """
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(userScore, computerScore):
  if userScore == computerScore:
    return "Draw"
  elif computerScore == 0:
    return "Lose, opponent has the Blackjack!"
  elif userScore == 0:
    return "Win with a Blackjack"
  elif userScore > 21:
    return "You lose!"
  elif computerScore > 21:
    return "You win"
  elif userScore > computerScore:
    return "You win"
  else:
    return "You lose!"


userCards = []
computerCards = []
userScore = 0
computerScore = 0
isGameOver = False

print(gameLogo.logo)

for _ in range(2):
  userCards.append(dealCard())
  computerCards.append(dealCard())

while not isGameOver:
  userScore = calculateScore(userCards)
  computerScore = calculateScore(computerCards)

  print(f"  Your cards: {userCards}, current score {userScore}")
  print(f"  Computer's first card: {computerCards[0]}")

  if userScore == 0 or calculateScore == 0 or userScore > 21:
    isGameOver = True
  else:
    userShouldDeal = input("type 'y' to get another card, type 'n' to pass: ")
    if userShouldDeal == 'y':
      userCards.append(dealCard())
    else:
      isGameOver = True

while computerScore != 0 and computerScore < 17:
  computerCards.append(dealCard())
  computerScore = calculateScore(computerCards)

print(f"  Your final hand: {userCards}, final score: {userScore}")
print(f"  Computer's final hand: {computerCards}, final score: {computerScore}")
print(compare(userScore, computerScore))
