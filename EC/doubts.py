'''
start = 0
stop  = 5-1 = 4
step  = +1
range(5)

start = 1
stop  = 11-1 = 10
step  = +1
range(1,11)

start = 1
stop  = 21-1 = 20
step  = +2
range(1,21,2)
# reverse loop
range(10,1,-1)
'''
'''
numbers = [4,5,3,3,0,1,24]
for i in numbers:
    if i == 0:
        continue
    result = 10 / i
    print(result)
'''

'''
chat = True
while chat:
    msg = input("Enter your message : ")
    if msg == "hi":
        print("hello user")
    elif msg == "bye":
        print("bye user")
        chat = False
    else:
        print("I don't understand")
'''

text = 'hello everyone, this is python programming'
'''
for i in range(len(text)):
    if text[i] == 'o':
        print(i)
'''

start = 0
count = text.count('o')
for i in range(count):
    index = text.index('o', start)
    start = index + 1
    print(index)
























