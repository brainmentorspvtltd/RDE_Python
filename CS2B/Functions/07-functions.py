def calc():
    x = 9
    y = 5
    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z

    return add, sub

output = calc()
print(output[0]())
print(output[1]())
