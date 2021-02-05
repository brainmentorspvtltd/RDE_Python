def temp_convert(c):
    return 9/5 * c + 32

# f = temp_convert(45.66)
# print(f)

temp = [23.3,37.6,29.8,27.8,30.5]
# temp_convert(temp[0])
converted = []
for i in range(len(temp)):
    f = temp_convert(temp[i])
    converted.append(f)

print(converted)