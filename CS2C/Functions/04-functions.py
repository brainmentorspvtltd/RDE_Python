# variable length arguments
def add(*x):
    print(x)
    count = 0
    for i in x:
        count = count + i
    print("Sum is",count)

add(4,5)
add(5,7,8,9)
add(1,2,3,6,7,8,5,3,3)
