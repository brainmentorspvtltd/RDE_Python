def calc(x,y,opr):
    z = x + opr + y
    print("Result is",eval(z))

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice : "))

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

operations = {
    1 : '+',
    2 : '-',
    3 : '/',
    4 : '*'
}

opr = operations[ch]
calc(num_1, num_2, opr)
