try:
    file = open('text_1.txt', 'r')
    data = file.read()
    print(data)
    file.write(data)
    # file.close()
except BaseException as ex:
    print(ex)
finally:
    print("File closed...")
    file.close()