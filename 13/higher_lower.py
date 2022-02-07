import random
from typing import List
from art import logo
from game_data import data as footbalers

def chooseBetweenOptions(question: str, options: List[str]):
  comma_separeted_options = ', '.join(options) 
  while True:
    chosen_option = input(f"{question} ({comma_separeted_options}): ")
    if options.count(chosen_option) > 0:
      return(chosen_option)
    else:
      print("Unknown operation. Try again!")

def askUserYesOrNo(question: str, yes = "yes", no = "no"):
  while True:
    user_desire_to_continue = input(f"{question} ({yes}) or ({no}): ")
    if user_desire_to_continue == yes:
      return True
    elif user_desire_to_continue == no:
      return False
    else:
      print("Unknown operation. Try again!")

def transformTo(first, second):
  return(
    {

    }
  )

print(logo)


[first_footballer_to_compare, second_footballer_to_compare] = random.choices(footbalers, k=2)

print(f"Compare A: {first_footballer_to_compare}")
print(f"Compare B: {second_footballer_to_compare}")

{
  "A": first_footballer_to_compare.follower_count >
}


chooseBetweenOptions("Who has more followers", ["A", "B"])