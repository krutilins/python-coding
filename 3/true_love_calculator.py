print("Welcome to true love calculator")
user_name = input("Type your name: ").lower()
crash_name = input("Type your's crash name: ").lower()

user_number = 0
crash_number = 0

for i in range(97, 123):
  print(chr(i))
  user_character_count = user_name.count(chr(i))
  crash_character_count = crash_name.count(chr(i))

  if user_character_count > crash_character_count:
    user_character_count = user_character_count - crash_character_count, 
    crash_character_count = user_character_count - ost
  else:
    ost = crash_character_count - user_character_count
    user_character_count = crash_character_count - ost

  user_number += user_character_count
  crash_number += crash_character_count

print(f"Your score is {user_number}{crash_number}")
  
