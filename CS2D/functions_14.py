def calc():
    x = 10
    y = 5

    def add():
        z = x + y
        # print("Sum is",z)
        return z
    def sub():
        z = x - y
        # print("Sub is",z)
        return z
    return add, sub
results = calc()
# print("Sum is",results[0]())
# print("Sub is",results[1]())
print(results)