a = 5
b = 2
c = a + b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {0} is {2}".format(a,b,c))

#f-strings
print(f"Sum of {a} and {b} is {c}")
