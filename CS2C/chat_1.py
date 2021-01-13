name = input("Enter your name : ")
print("Welcom",name,"Ask me anything...")

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey":
        print(msg,name)
    elif msg == "bye":
        print("Bye",name,"Take care...")
        chat = False
    else:
        print("I don't understand")
