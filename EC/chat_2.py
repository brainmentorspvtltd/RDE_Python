chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg == "hello":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
