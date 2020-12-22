a,b = 5,10
#a,b = b,a

#walrus operator
#print(c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)} ")

print(f"""
Addition is {(c := a + b)}
Subtraction is {(d := a - b)}
Division is {(e := a / b)}
Multiplication is {(f := a * b)}
""")
