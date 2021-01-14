from datetime import datetime as dt
import os, random

name = input("Enter your name : ")
print("Welcome {}, Ask me anything...".format(name))

helloIntent = ["hello","hi","hey","hi there","hello there","howdy"]
dateIntent = ["date", "date please", "please tell me date",
              "today's data", "what' the date today"]
timeIntent = ["time", "time please", "please tell me time",
              "current time", "what' the time"]
musicIntent = ["play song", "play music", "start song"]

chat = True
while chat:
    msg = input(">> ")
    # membership operator - in, not in
    # identity operator  - is, is not
    if msg in helloIntent:
        print("{} {}".format(msg,name))
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime('%d/%m/%y, %a'))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime('%H:%M:%S, %p'))
    elif msg in musicIntent:
        path = r'C:\Users\acer\Music'
        os.chdir(path)
        songs = os.listdir()
        for i in range(len(songs)):
            print(i+1, songs[i])
        num = int(input("Enter song number you want to play : "))
        song = songs[num-1]
        os.startfile(song)
    elif msg == "bye":
        print("Bye {}, Take care".format(name))
        chat = False
    else:
        print("I don't understand...")
