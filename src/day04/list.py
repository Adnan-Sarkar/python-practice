# list
fruits = ["Mango", "Apple", "Banana", "Orange", "Strawberrie"]

print(fruits)

# list item starts with index 0
print(fruits[0])
print(fruits[1])

# negative index starts with end
print(fruits[-1])
print(fruits[-2])

# change any item of the list
fruits[0] = "Watermelon"

print(fruits)
print(fruits[0])

# add new item at end of the list
fruits.append("Grape")
print(fruits)

# extend a list with another list
fruits.extend(["Lychee", "Cherrie"])
print(fruits)