def sum(number_list):
    for s in number_list:
        sum = 0
        n = int(input("Enter the number of number:"))
        for i in range(n):
            mark = int(input("{0}:".format(s)))
            sum = sum + mark
        print(s,"sum is :",sum)


num1 = ["number"]
sum(num1)