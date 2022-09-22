def galon_litr (n):
    return n * 3.785

print("input the galon number :\nfor finish input negetive number")
while True:
    n = int(input())
    if n >= 0:
        print(galon_litr(n))
    else:
        print("finish")
        break






