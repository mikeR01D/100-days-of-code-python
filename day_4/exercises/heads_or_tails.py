# import the randomint module
import random

# set the randint between the range of 0 and 1
toss = random.randint(0, 1)
print(toss)
# if the randomint is 0, print head
if toss == 0:
    print("Head")

# else, print tail
else:
    print("Tail")