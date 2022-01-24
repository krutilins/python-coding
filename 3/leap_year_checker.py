year = int(input("Type a year"))

if year % 4 == 0 & (year % 100 != 0 | year % 400 == 0):
  print("Leap Year")
else:
  print("Not Leap Year")