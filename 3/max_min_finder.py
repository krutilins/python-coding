first = int(input("Type first number: "))
second = int(input("Type second number: "))
third = int(input("Type third number: "))

if first >= second and first >= third:
  print(f"Maximum: {first}")
elif second >= first and second >= third:
  print(f"Maximum: {second}")
else:
  print(f"Maximum: {third}")

if first <= second and first <= third:
  print(f"Minimum: {first}")
elif second <= first and second <= third:
  print(f"Minimum: {second}")
else:
  print(f"Minimum: {third}")

