import math
row = int(input("Enter numbers of rows :"))
col = int(input("Enter numbers of cols :"))

for i in range(row):
    for j in range(col):
        if (i + j) %2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()
