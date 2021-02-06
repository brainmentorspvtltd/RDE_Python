file = open('data_types.png', 'rb')
data = file.read()
print(data)
file.close()

file = open('data_types_2.png', 'wb')
file.write(data)
file.close()
