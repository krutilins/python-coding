MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def chooseBetweenOptions(question: str, options: List[str]):
  comma_separeted_options = ', '.join(options) 
  while True:
    chosen_option = input(f"{question} ({comma_separeted_options}): ")
    if options.count(chosen_option) > 0:
      return(chosen_option)
    else:
      print("Unknown operation. Try again!")

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


chosen_option = chooseBetweenOptions("What would you like?", ["espresso", "latte", "cappuccino"])
process_coins()