import random

row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']

map = [row1, row2, row3]

random_row = random.randint(0, 2)
random_column = random.randint(0, 2)

map[random_row][random_column] = "🟩"

user_input = str(input("Which one do you want to open? (row, column)"))
row, column = int(user_input[0]), int(user_input[1])



if map[row][column] == '🟩':
  print("You found a treasure")
else:
  map[row][column] = "🟥"
  print("Sorry, you loose you chance")

print(map[0])
print(map[1])
print(map[2])
