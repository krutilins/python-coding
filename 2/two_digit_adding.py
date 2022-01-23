# two digit adding 
# gets two digit number and returns sum of this digits

two_digit_number_string = str(input("Type a two digit number\n"))
first_digit, second_digit = int(two_digit_number_string[0]), int(two_digit_number_string[1])
print(first_digit + second_digit)