def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

temp = [43.3,27.8,29.4,32.4,32.7]
kms = [45,44,2,57,8,5.6]
ms = [1212,1145,5677,3578]

def my_map(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

data = my_map(temp_convert, temp)
print(data)

data = my_map(km_to_m, kms)
print(data)

data = my_map(m_to_km, ms)
print(data)


