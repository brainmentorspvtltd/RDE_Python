#fib series - 0,1,1,2,3,5,8,13,21

# swapping of two numbers
'''
a,b = 10,20
a,b = b,a
'''
a = 1
b = 0
while b < 100:
    print(b,end=',')
    a,b = b,a+b
