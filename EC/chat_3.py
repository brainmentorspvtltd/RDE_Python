from datetime import datetime as dt

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello User")
    elif msg == "date":
        d = dt.now().date()
        print(d.strftime('%d/%m/%y, %a'))
    elif msg == "time":
        t = dt.now().time()
        print(t.strftime('%H/%M/%S, %p'))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
