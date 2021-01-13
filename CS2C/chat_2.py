from datetime import datetime as dt

name = input("Enter your name : ")
print("Welcom",name,"Ask me anything...")

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey":
        print(msg,name)
    elif msg == "time":
        t = dt.now().time()
        print(t.strftime('%H:%M:%S, %p'))
    elif msg == "date":
        d = dt.now().date()
        print(d.strftime('%d-%b-%y, %A'))
    elif msg == "bye":
        print("Bye",name,"Take care...")
        chat = False
    else:
        print("I don't understand")
