def get_fiz_buzz_string(value):
  print_string = ""
  if i % 3 == 0:
    print_string += "fizz"
  if i % 5 == 0:
    print_string += "buzz"
  return print_string

for i in range(0, 100):
  print_string = get_fiz_buzz_string(i)
  if print_string != "":
    print(print_string)
  else:
    print(i)

