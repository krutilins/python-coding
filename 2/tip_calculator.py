print("Welcome to tip calculator")
totall_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_count = int(input("How many people to split the bill? \n"))
each_person_pay = (totall_bill + totall_bill * percentage_tip / 100) / people_count
print(f"Each person should pay: {round(each_person_pay, 2)}")