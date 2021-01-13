from datetime import datetime as dt
import os, random

name = input("Enter your name : ")
print("Welcome",name)

chat = True

while chat:
    msg = input("Enter your message : ")
    #logical operators - and, or, not
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello",name)
    elif msg == "date":
        d = dt.now().date()
        print(d.strftime('%d-%b-%y, %A'))
    elif msg == 'play music':
        os.chdir(r'C:\Users\acer\Music')
        songs = os.listdir()
        s = random.choice(songs)
        os.startfile(s)
    elif msg == 'time':
        t = dt.now().time()
        print(t.strftime('%H:%M:%S, %p'))
    elif msg == "bye":
        print("Bye",name,"Take care...")
        chat = False
    else:
        print("I don't understand")
