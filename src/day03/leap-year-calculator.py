year = int(input("Enter year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is Leap Year")
    else:
      print(f"{year} is not Leap Year")
  else:
    print(f"{year} is Leap Year")
else:
  print(f"{year} is not Leap Year")