# life in days, weeks, months calculator
import constants

user_age = int(input("how old are you?\n"))
years_remaining = constants.YEARS_IN_LIFE - user_age
months_remaining = years_remaining * constants.MONTHS_IN_YEAR
weeks_remaining = years_remaining * constants.WEEKS_IN_YEAR
days_remaining = years_remaining * constants.DAYS_IN_YEAR
print(f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days")

