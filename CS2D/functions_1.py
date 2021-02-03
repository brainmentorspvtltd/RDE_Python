x = 5
y = 6
def add():
    # local variables
    global x
    global y
    x = 10
    y = 12
    z = x + y
    print("Sum is",z)

def sub():
    z = x - y
    print("Sub is",z)

add()
sub()
