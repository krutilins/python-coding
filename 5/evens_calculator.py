range_length = int(input("Type range length: "))

even_sum = 0

for i in range(0, range_length, 2):
  even_sum += i

print(f"Sum of evens in range from 0 to {range_length} is equal {even_sum}")