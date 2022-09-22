from random import randrange


def roll():
    return randrange(1,7)


while True:
    x = roll()
    print(x)
    if x == 6:
        break