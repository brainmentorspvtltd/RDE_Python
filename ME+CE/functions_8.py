# def temp_convert(c):
#     return 9/5 * c + 32

temp = [23.3,37.6,29.8,27.8,30.5]
converted = list(map(lambda c : 9/5 * c + 32, temp))
print(converted)
