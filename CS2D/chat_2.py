name = input("Enter your name : ")
print("Welcome {}, Ask me anything...".format(name))

chat = True
while chat:
    msg = input(">> ")
    #Comparison Operator - ==, !=, >,<, >=, <=
    #Logical Operators - and, or, not
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("{} {}".format(msg,name))
    elif msg == "bye":
        print("Bye {}, Take care".format(name))
        chat = False
    else:
        print("I don't understand...")
