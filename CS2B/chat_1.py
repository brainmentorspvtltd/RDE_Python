from datetime import datetime as dt
import os, random

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
    elif msg == "time":
        time = dt.now().time()
        print("Time",time.strftime('%H:%M:%S, %p'))
    elif msg == "play music" or msg == "play song":
        # 1. change directory where we have songs
        os.chdir('C:/Users/acer/Music')
        # 2. Get all the files available in that directory
        songs = os.listdir()
        # 3. Pick any random song from list of songs
        song = random.choice(songs)
        # 4. Start the file that is selected randomly
        print("Playing :",song)
        os.startfile(song)
    elif msg == 'show songs':
        os.chdir('C:/Users/acer/Music')
        songs = os.listdir()
        for i in range(len(songs)):
            print(i+1, songs[i])
        num = int(input("Enter the song number you want to play : "))
        song = songs[num - 1]
        os.startfile(song)
        
    elif msg == "bye":
        print(f"Bye {name}, Take Care...")
        chat = False
    else:
        print("I don't understand")
