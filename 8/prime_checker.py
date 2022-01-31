from math import floor, sqrt


def is_prime(number):
  if number > 1:
    for i in range(2, int(floor(sqrt(number) + 1))):
      if number % i == 0:
        return(False)
  return(True)

n = int(input("Check this number: "))
if is_prime(number = n):
  print(f"Number {n} is prime")
else:
  print(f"Number {n} is not prime")
