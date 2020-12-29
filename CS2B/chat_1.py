from datetime import datetime as dt

name = input("Enter your name : ")
print("Welcome",name)

chat = True
while chat:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("{} User".format(msg))
    elif msg == 'date':
        date = dt.now().date()
        print(date.strftime('%d/%m/%y, %a'))
    elif msg == "bye":
        print(f"Bye {name}, Take Care...")
        chat = False
    else:
        print("I don't understand")
