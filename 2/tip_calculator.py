print("Welcome to tip calculator")
totall_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_count = int(input("How many people to split the bill? \n"))
bill_per_person = (totall_bill + totall_bill * percentage_tip / 100) / people_count
formated_bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {formated_bill_per_person}")