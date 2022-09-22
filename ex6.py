import math

def get_value(d, p):
    return p / (math.pi * math.pow((d/2), 2))

first_pizza_list = input("Input 1st pizza's diameter and price: (E.g. 5 7) ").split(" ")
second_pizza_list = input("Input 2nd pizza's diameter and price: (E.g. 5 7) ").split(" ")

first_pizza = get_value(int(first_pizza_list[0]), int(first_pizza_list[1]))
second_pizza = get_value(int(second_pizza_list[0]), int(second_pizza_list[1]))

print("first_pizza") if first_pizza > second_pizza else print("second_pizza")