name = input("Enter your name : ")
print("Hello",name)

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == 'hello' or msg == 'hi' or msg == 'hey':
        print(msg,name)
    elif msg == 'bye':
        print("Bye, Take Care")
        chat = False
    else:
        print("I don't understand")
