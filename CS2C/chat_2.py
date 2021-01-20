from datetime import datetime as dt
import os, random

name = input("Enter your name : ")
print("Welcome",name,"Ask me anything...")

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey":
        print(msg,name)
    elif msg == 'play song':
        os.chdir(r'C:\Users\acer\Music')
        songs = os.listdir()
        song = random.choice(songs)
        print("Playing :",song)
        os.startfile(song)
    elif msg == "show songs":
        os.chdir(r'C:\Users\acer\Music')
        songs = os.listdir()
        for i in range(len(songs)):
            print(i+1, songs[i])
        num = int(input("Enter the song number you want to play : "))
        print("Playing Track :",songs[num - 1])
        os.startfile(songs[num - 1])
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
