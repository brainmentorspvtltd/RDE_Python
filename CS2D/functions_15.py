def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

# f = temp_convert(34.5)
# print(f)

temp = [43.3,27.8,29.4,32.4,32.7]
converted = []
for t in temp:
    f = temp_convert(t)
    converted.append(f)

print(converted)

kms = [4.5,4.3,3,5.8]
converted = []
for km in kms:
    m = km_to_m(km)
    converted.append(m)

print(converted)