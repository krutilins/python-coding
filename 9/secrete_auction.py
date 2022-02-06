bid_log = {}

def add_bid(name: str, bid: int):
  bid_log[name] = bid

next_user = True
while next_user:
  name = input("What's your name?")
  bid = int(input("What's your bid?"))

  add_bid(name, bid)

  user_answer = input("Do you want to add a new bid? \"yes\" or \"no\"")
  if user_answer == "yes":
    next_user = True
  elif user_answer == "no":
    next_user = False
  else:
    print("I don't know such answer")
    next_user = False

user_with_highest_bid = ""
highest_bid = 0
for key in bid_log:
  if bid_log[key] > highest_bid:
    highest_bid = bid_log[key]
    user_with_highest_bid = key
print(f"{user_with_highest_bid}: {highest_bid}")