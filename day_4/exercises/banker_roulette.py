import random

names_string = input("Give me everybody's name, seperated by a comma and a space: ")
names = names_string.split(", ")
print(names)

random_int= random.randint(0, int(len(names) - 1))
print(random_int)

person_to_pay = names[random_int]
print(f"{person_to_pay} is the person that is paying for the meal! ")