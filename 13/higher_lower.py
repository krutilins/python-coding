from ssl import Options
from typing import List
from art import logo

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


print(logo)

chooseBetweenOptions("What do you prefer?", ['cake', 'milk', 'coffee', 'die'])

print("Compare A: ")