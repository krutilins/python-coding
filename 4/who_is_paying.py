import random 

print("Welcome to Who is Paying")

all_users = input("Type names separated by comma and space: ").split(', ')

payer_name = all_users[random.randint(0, len(all_users) - 1)]

print(f"{payer_name} is paying!!!")

