class Question:
  def tryAnswer(self):
    return(self.answer is self.chooseBetweenOptions())

  def chooseBetweenOptions(self):
    print(self.options)
    comma_separeted_options = ', '.join(self.options) 
    while True:
      chosen_option = input(f"{self.question} ({comma_separeted_options}): ")
      if self.options.count(chosen_option) > 0:
        return(chosen_option)
      else:
        print("Unknown operation. Try again!")

  def __init__(self, question, answer, incorrect_options):
    self.question = question
    self.answer = answer
    incorrect_options.append(answer)
    self.options = incorrect_options

q1= Question("2 + 3 = 5", "True", ["False"])

if q1.tryAnswer():
  print("You are right!")
else:
  print("You are wrong!") 
