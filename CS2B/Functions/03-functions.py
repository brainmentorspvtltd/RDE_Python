# *args - variable length argument
def product(*x):
    # print(x)
    count = 1
    for item in x:
        count *= item
    print("Product is",count)

product(2,3)
product(4,3,5)
product(3,4,6,8,2,4)
product(3,6,7,8,4,4,67,8)

