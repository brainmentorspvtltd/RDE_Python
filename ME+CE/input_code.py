# by default python takes input in string type
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
name = first_name + " " + last_name
print("Hello",name)

# so we need to type cast the input function
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
res = num_1 + num_2
print("Sum is",res)
