import game_elements
import random

user_choose = input("Paper? Rock? Scissors?\n")

if user_choose == game_elements.ROCK:
    print(game_elements.ROCK_HAND)
elif user_choose == game_elements.PAPER:
    print(game_elements.PAPER_HAND)
elif user_choose == game_elements.SCISSORS:
    print(game_elements.SCISSORS_HAND)
else:
    print("You choose incorrect option!")

computer_choose = [game_elements.ROCK, game_elements.PAPER, game_elements.SCISSORS][random.randint(0, 2)]

print("Computer choice: ")
if computer_choose == game_elements.ROCK:
    print(game_elements.ROCK_HAND)
elif computer_choose == game_elements.PAPER:
    print(game_elements.PAPER_HAND)
elif computer_choose == game_elements.SCISSORS:
    print(game_elements.SCISSORS_HAND)

