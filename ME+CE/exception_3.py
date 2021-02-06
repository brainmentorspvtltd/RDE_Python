try:
    file = open('text_1.txt', 'r')
    data = file.read()
    file.write(data)
    # file.close()
except BaseException as ex:
    print(ex)
else:
    print(data)
finally:
    print("File closed...")
    file.close()