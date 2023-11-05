import random

a = int(input("how many numbers do you want? "))
n = []
for t in range(a):
    b = (random.randint(1,100))
    if b not in n:
        n.append(b)

print(n)