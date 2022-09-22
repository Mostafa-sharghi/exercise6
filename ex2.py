from random import randrange


def roll(n):
    return randrange(n)+1


n = int(input("input number of roll:"))

while True:
    x = roll(n)
    print(x)
    if x == n:
        break