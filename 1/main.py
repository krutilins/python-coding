# input/output practice
learning_subject = input("What are you learning right now?\n")
print("You are bad at learning " + learning_subject)

future_goal = input("What goald do you want to set for yourself?\n")
print("You will never become a professional at " + future_goal)

user_name = input("What's your name?\n")
print(len(user_name))

# swap practice

a = input("Enter A value\n")
b = input("Enter B value\n")

# swapping values manually
# temp = b
# b = a
# a = temp

a, b = b, a

print("A = " + a, ", while B = " + b)

# brand name generator

favorite_ice_cream = input("What is your favorite ice-cream?\n")
pet_name = input("What is your pet's name?\n")
print("You brand name could be " + favorite_ice_cream + pet_name)
