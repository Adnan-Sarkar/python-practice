# and
examMark = 70
if examMark > 80 and examMark <= 100:
  print("Your grade is: A")
elif examMark > 70 and examMark <= 80:
  print("Your grade is: B")
elif examMark > 60 and examMark <= 70:
  print("Your grade is: C")
elif examMark > 50 and examMark <= 60:
  print("Your grade is: D")
else:
  print("Your grade is: F")

# or
color = "blue"
if color == "blue" or color == "green":
  print("Welcome to the playground")
else:
  print("Welcome to the classroom")

# not
isStudent = False
if not isStudent:
  print("Sorry, you can't enter the school")
else:
  print("Welcome to the school")