height = float(input('enter your height in meters: '))
weight = float(input('enter your weight in kilograms: '))

bmi = weight/(height * height)

if bmi < 18.5:
    print('Your BMI is under 18.5, you are underweight')

if bmi >= 18.5:
  
    print("Your BMI is ")
