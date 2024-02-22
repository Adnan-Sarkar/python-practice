print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"));

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tipPercent = tip / 100
totalTipAmount = bill * tipPercent
totalBill = bill + totalTipAmount

numberOfPeoples = int(input("How many people to split the bill? "))

billPerPerson = round(totalBill / numberOfPeoples, 2)
billPerPerson = "{:.2f}".format(billPerPerson)

print(f"Each person should pay: ${billPerPerson}")