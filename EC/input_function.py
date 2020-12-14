# by default python input() return string type of data 
'''
name = input("Enter your name : ")
print("Hello",name)
'''

print("Hello",name := input("Enter your name : "))

# so we need to type cast/convert the input()
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = x + y
print("Sum is",z)
