import random
import testModule

# generate random number between 1 and 10
randomInt = random.randint(1, 10)
print(randomInt)

# generate random floating number between 0.0 and 1.0, but 1.0 is exclude
randomFloat = random.random()
print(randomFloat)

# using testModule file
print(testModule.name)