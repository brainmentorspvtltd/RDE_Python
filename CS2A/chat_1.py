name = input("Enter your name : ")
print("Welcome",name)

chat = True

while chat:
    msg = input("Enter your message : ")
    #logical operators - and, or, not
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello",name)
    elif msg == "bye":
        print("Bye",name,"Take care...")
        chat = False
    else:
        print("I don't understand")
