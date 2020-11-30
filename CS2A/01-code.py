a = 3
b = 4
c = a + b
d = a - b
e = a / b
f = a * b

print("Sum is",c)
print("Sum of",a,"and",b,"is",c)
print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))
print("Sum of {} and {} is {}".format(a,b,c))
#f-strings
print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a=} and {b=} is {c=}")
#Multi line print
print(f"""
1. Add is {c}
2. Sub is {d}
3. Div is {e}
4. Mul is {f}
""")
