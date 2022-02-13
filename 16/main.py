from typing import List

def chooseBetweenOptions(question: str, options: List[str]):
  comma_separeted_options = ', '.join(options) 
  while True:
    chosen_option = input(f"{question} ({comma_separeted_options}): ")
    if options.count(chosen_option) > 0:
      return(chosen_option)
    else:
      print("Unknown operation. Try again!")


class Question:
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer

q1= Question("2 + 3 = 5", "True")

if q1.answer is chooseBetweenOptions(q1.question, ["True", "False"]):
  print("You are right!")
else:
  print("You are wrong!") 
