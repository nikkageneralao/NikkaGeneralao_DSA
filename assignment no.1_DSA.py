# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# ASSIGNMENT NO. 1
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

str1 = "PAU"
forP = [[" " for i in range (5)] for j in range (6)]
forA = [[" " for i in range (5)] for j in range (6)]
forU = [[" " for i in range (5)] for j in range (6)]

# for P
for row in range(6):
    for col in range(5):
        if ((col == 0 or (col == 4 and (row == 1 or row == 2))) or ((row == 0 or row == 3) and (col != 0 and col != 4))):
            forP[row][col]="*"

# for A
for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 0) or (row == 0 or row == 3) and (col != 0 and col != 4):
            forA[row][col] = "*"

# for U
for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 5) or (row == 5 and (col != 0 and col != 4)):
            forU[row][col] = "*"

for i in range (6):
    for j in range (5):
        print(forP[i][j], end = " ")
    print (end = "  ")
    for j in range (5):
        print(forA[i][j], end = " ")
    print(end="  ")
    for j in range (5):
        print(forU[i][j], end = " ")
    print()

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-