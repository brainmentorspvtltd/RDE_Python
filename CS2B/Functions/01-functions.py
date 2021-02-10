x = 10
y = 20
# Function Definition
def calc():
    # Local Variables
    global x,y
    x = 5
    y = 6
    z = x + y
    print("Sum is",z)
# Function Calling
calc()
z = x - y
print("Diff is",z)
