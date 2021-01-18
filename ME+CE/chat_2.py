import os, random

name = input("Enter your name : ")
print("Hello",name)

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == 'hello' or msg == 'hi' or msg == 'hey':
        print(msg,name)
    elif msg == 'play music':
        os.chdir(r'C:\Users\acer\Music')
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
        
    elif msg == 'show songs':
        os.chdir(r'C:\Users\acer\Music')
        songs = os.listdir()
        for i in range(len(songs)):
            print(i+1, songs[i])
        user_choice = int(input("Enter the song you want to play : "))
        song = songs[user_choice - 1]
        print("Playing", song)
        os.startfile(song)

    elif msg == 'bye':
        print("Bye, Take Care")
        chat = False
    else:
        print("I don't understand")
