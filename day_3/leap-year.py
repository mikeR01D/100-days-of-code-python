year = int(input('What year do you want to check?'))

# check if year is a factor of 4
if year % 4 == 0:
    # check if year is a factor of 4 but not a factor of 100
    if year % 100 != 0:
        # check if yea is a factor of 4, but not a factor of 100, yet still a factor of 400
        if year % 400 == 0:
            # print this if all conditions are met
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")

else:
     print("The year is not a leap year. ")
#  finally, check if the year is divisible by 400, and if so, it is without a shadow of a doubt that