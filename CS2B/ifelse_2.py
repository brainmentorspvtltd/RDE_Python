chat = True
while chat:
    msg = input("Enter your message : ")
    if msg == "hello":
        print("Hello User")
    elif msg == "bye":
        print("Bye User, Take Care...")
        chat = False
    else:
        print("I don't understand")
