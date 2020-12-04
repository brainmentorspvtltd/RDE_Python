a = 34
b = 12
c = a + b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))

#f-strings (fast-strings)
print(f"Sum of {a} and {b} is {c}")

d = a - b
e = a / b
f = a * b

print(f"""
1. Add is {c}
2. Sub is {d}
3. Div is {e}
4. Mul is {f}
""")








