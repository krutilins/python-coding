from unittest import result
from logo import logo

print(logo)

def askUserYesOrNo(question: str, yes = "yes", no = "no"):
  while True:
    user_desire_to_continue = input(f"{question} ({yes}) or ({no})")
    if user_desire_to_continue == yes:
      return True
    elif user_desire_to_continue == no:
      return False
    else:
      print("Unknown operation. Try again!")

def get_operation():
  while True:
    operation = input("Pick an operation (+, -, /, *): ")
    if operation == "/" or operation == "*" or operation == "+" or operation == "-":
      return operation
    else:
      print("Unknown operation. Try again!")

def perform_calculation(operation, first_number, second_number):
  if operation == "/":
    return first_number / second_number
  elif operation == "*":
    return first_number * second_number
  elif operation == "+":
    return first_number + second_number
  elif operation == "-":
    return first_number - second_number
  else:
    print("Unknown operation. Try again!")

def calculator():
  can_continue = True

  while can_continue:
    first_number = float(input("What's the first number? "))
    operation = get_operation()
    second_number = float(input("What's the second number? "))

    result = perform_calculation(operation, first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")

    can_continue = askUserYesOrNo("Do you want to continue?")

calculator()