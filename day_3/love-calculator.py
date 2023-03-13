print("Welcome to the Loce Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# convert the input to all lowercase

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

# combine all lowercase characters into a single string
combined_names = name1_lowercase + name2_lowercase

# count the number of times the following letters appears in each
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

print(f'T occurs {t} times')
print(f'R occurs {r} times')
print(f'U occurs {u} times')
print(f'T occurs {e} times')

true_total = t + r + u + e
print(f"Total = {true_total}")


