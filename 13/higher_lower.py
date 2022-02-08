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

score = 0

print(logo)
while True:
  [first_person_to_compare, second_person_to_compare] = random.choices(footbalers, k=2)

  print(f"Compare A: {first_person_to_compare['name']} - {first_person_to_compare['description']} - {second_person_to_compare['country']}")
  print(f"Compare B: {second_person_to_compare['name']} - {second_person_to_compare['description']} - {second_person_to_compare['country']}")

  if first_person_to_compare['follower_count'] > second_person_to_compare['follower_count']:
    answer_score_hash = {
      "A": 1,
      "B": -1
    }
  else:
    answer_score_hash = {
      "A": -1,
      "B": 1
    }

  score += answer_score_hash[chooseBetweenOptions("Who has more followers", ["A", "B"])]

  print(f"Your current score: {score}")