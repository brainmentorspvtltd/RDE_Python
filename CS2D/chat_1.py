name = input("Enter your name : ")
print("Welcome {}, Ask me anything...".format(name))

chat = True
while chat:
    msg = input(">> ")
    #Comparison Operator - ==, !=, >,<, >=, <=
    if msg == "hello":
        print("Hello {}".format(name))
    elif msg == "bye":
        print("Bye {}, Take care".format(name))
        chat = False
    else:
        print("I don't understand...")
