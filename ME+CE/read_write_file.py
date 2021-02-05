# 1. open file
# 2. read/write
# 3. close
# by default file open in read mode
# file = open('text_1.txt')
# data = file.read()
# print(data)
# file.close()

file = open('text_2.txt', 'w')
# data = file.write("hello world this is python programming")
file.write("Bye World")
# print(data)
file.close()
