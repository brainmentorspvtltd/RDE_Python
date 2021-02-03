def add(x,y):
    z = x + y
    print("Sum is",z)
def sub(x,y):
    z = x - y
    print("Sub is",z)
def div(x,y):
    z = x / y
    print("Div is",z)
def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice : "))

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {
    1 : add,
    2 : sub,
    3 : div,
    4 : mul
}

operations[ch](num_1, num_2)
