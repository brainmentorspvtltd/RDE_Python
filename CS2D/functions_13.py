def counter():
    x = 0
    while True:
        x += 1
        yield x

count = counter()
print(next(count))

print("="*20)

for i in count:
    print(i)
    if i == 20:
        break

print("="*20)
print(next(count))
