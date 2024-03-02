user = {
  "name": "Adnan Sarkar",
  "age": 50,
}

# retrieving items from dictionary
print(user["name"])

# adding new items to the dictionary
user["email"] = "demo@gmail.com"

# edit an item in the dictionary
user["age"] = 55

# loop through a dictionary
for key in user:
  print(key)
  print(user[key])

print(user)