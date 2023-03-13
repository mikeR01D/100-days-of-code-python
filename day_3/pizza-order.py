print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L?  ")
add_pepperoni = input("Do you want pepperoni? (Y/N)")
extra_cheese = input("Do you want extra cheese? (Y/N)")

# initialize the variable 'bill' with 0
bill = 0


if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is ${bill}. ")
        else:
            print(f"Your final bill is ${bill}. ")
    elif extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}. ")
    else:
        print(f"Your final bill is ${bill}. ")


elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is ${bill}. ")
        else:
            print(f"Your final bill is ${bill}. ")
    elif extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}. ")
    else:
        print(f"Your final bill is ${bill}. ")

else:
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is ${bill}. ")
        else:
            print(f"Your final bill is ${bill}. ")
    elif extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}. ")
    else:
        print(f"Your final bill is ${bill}. ")
