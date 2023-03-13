row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_int = int(position)

# divide input by 10 in order to seperate the input into their respective row and column
position_column = position_int/10
position_row = position_int % 10

# replace the box that lies in 'position_column' and 'position_row' with 'X'
marked_map = map[int(position_row - 1)][int(position_column -1)] = 'X'
print(marked_map)





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")