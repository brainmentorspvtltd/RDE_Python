a = 5
b = 6

#walrus operator - :=
#print(c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
1. Sum is {(c := a + b)}
2. Sub is {(d := a - b)}
3. Div is {(e := c / d)}
4. Mul is {(f := e * d)}
""")
