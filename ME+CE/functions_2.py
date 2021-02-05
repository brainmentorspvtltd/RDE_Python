# global variables
#x = 6
#y = 10

def add():
    #local variables
    x = int(input("Enter first num : "))
    y = int(input("Enter second num : "))
    z = x + y
    print("Sum is",z)

def sub():
    #local variables
    #x = int(input("Enter first num : "))
    #y = int(input("Enter second num : "))
    z = x - y
    print("Sub is",z)

#result = x * y
#print("Result is",result)

print("""
1. Press 1 for Add
2. Press 2 for Sub
""")

choice = input("Enter your choice : ")
if choice == "1":
    add()
elif choice == "2":
    sub()
else:
    print("Invalid Choice")






