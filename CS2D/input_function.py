# by default  python input() returns string type of data
'''
name = input("Enter your name : ")
print("Hello",name)
'''

print("Hello",name := input("Enter your name : "))

# so we need to type cast input function
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = x + y
print("Sum is",z)
