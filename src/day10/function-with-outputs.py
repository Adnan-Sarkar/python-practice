# functions with output
def formatName(firstName, lastName):
  formatedFirstName = firstName.title()
  formatedLasrName = lastName.title()
  return f"{formatedFirstName} {formatedLasrName}"

formatString = formatName("adnan", "sarkar")
print(formatString)