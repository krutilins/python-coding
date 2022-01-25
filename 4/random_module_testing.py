import random

randomNumbers = []

for i in range(0, 10):
  randomNumbers.append(random.randint(0, 10))

print(randomNumbers)


randomFloatNumbers = []

for i in range(0, 10):
  randomFloatNumbers.append(random.random())

print(randomFloatNumbers)