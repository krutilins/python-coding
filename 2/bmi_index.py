# bmi index
def get_weight_status(bmi_index):
  if 18.5 > bmi_index:
    return("Underweight") 
  elif 24.9 > bmi_index:
    return("Healthy")
  elif 29.9 > bmi_index:
    return("Overweight")
  else:
    return("Obese")

def get_bmi_index(weight, height):
  return(weight / height ** 2)

user_weight = float(input("Type your weight (kilograms): \n"))
user_height= float(input("Type your height (metres): "))

bmi_index = get_bmi_index(user_weight, user_height)
weight_status = get_weight_status(bmi_index)

print("BMI Index is equal " + str(bmi_index))
print("Your weight statuse is " + weight_status)