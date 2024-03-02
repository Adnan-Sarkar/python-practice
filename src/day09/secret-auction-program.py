from auction_logo import logo

biddingList = []

def addBidding(userName, biddingPrice):
  newBidding = {}
  newBidding["name"] = userName
  newBidding["bid_price"] = biddingPrice
  biddingList.append(newBidding)

def findBiddingWinner(biddingList):
  maxBidPrice = 0
  bidWinnerDetails = {}
  for bidder in biddingList:
    if bidder["bid_price"] > maxBidPrice:
      maxBidPrice = bidder["bid_price"]
      bidWinnerDetails = bidder

  print(f'The winner is {bidWinnerDetails["name"]} with a bid of ${bidWinnerDetails["bid_price"]}')

# display logo
print(logo)

while True:
  name = input("What is your name?\n")
  bidPrice = int(input("What is your bid?\n"))
  addBidding(userName=name, biddingPrice=bidPrice)

  wantToBid = input("Are there any other bidders? type 'yes' or 'no'\n")
  if wantToBid == "no":
    # find bidding winner
    findBiddingWinner(biddingList)
    break



