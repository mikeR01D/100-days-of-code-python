age = input("What is your current age? ")

# convert age to its int equivalent
int_age = int(age)

# since average lifespan is 90, we substract the inputted age from it, i.e 90 - 34
remaining_years = 90 - int_age

# convert the remaining years left to its equivalent in month, weeks and days
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

# output the value
print(f'You have {remaining_days} days left, {remaining_weeks} weeks left, and {remaining_months} months left.')
