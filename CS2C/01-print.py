a = 5
b = 6
c = a + b
print(c)
print("Sum is",c,sep=',')
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {2} and {1} is {0}".format(c,b,a))

#f-strings (fast-strings)
print(f"Sum of {a} and {b} is {c}")
