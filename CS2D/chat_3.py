from datetime import datetime as dt
import os, random

name = input("Enter your name : ")
print("Welcome {}, Ask me anything...".format(name))

chat = True
while chat:
    msg = input(">> ")
    #Comparison Operator - ==, !=, >,<, >=, <=
    #Logical Operators - and, or, not
    if msg == "hello" or msg == "hi" or msg == "hey":
        print("{} {}".format(msg,name))
    elif msg == 'date':
        current_date = dt.now().date()
        print(current_date.strftime('%d/%m/%y, %a'))
    elif msg == 'time':
        current_time = dt.now().time()
        print(current_time.strftime('%H:%M:%S, %p'))
    elif msg == 'play music':
        path = r'C:\Users\acer\Music'
        os.chdir(path)
        songs = os.listdir()
        '''
        song = random.choice(songs)
        os.startfile(song)
        '''
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
