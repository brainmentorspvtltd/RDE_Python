Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_2.py =====
Enter your message : hello
Hello User
>>> 
===== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_2.py =====
Enter your message : hello
Hello User
Enter your message : hi
I don't understand
Enter your message : bye
Bye User
>>> 
===== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_2.py =====
Enter your message : Hello
I don't understand
Enter your message : bye
Bye User
>>> 
===== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_2.py =====
Enter your message : HeLLo
Hello User
Enter your message : bye
Bye User
>>> 
===== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_3.py =====
Enter your message : hi
Hello User
Enter your message : hello
Hello User
Enter your message : hey
Hello User
Enter your message : bye
Bye User
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2021, 1, 22, 12, 18, 19, 864238)
>>> datetime.datetime.now().date()
datetime.date(2021, 1, 22)
>>> datetime.datetime.now().time()
datetime.time(12, 18, 47, 262713)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 1, 22, 12, 19, 59, 923944)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2021, 1, 22, 12, 20, 17, 837579)
>>> d = dt.now().date()
>>> t = dt.now().time()
>>> print(d)
2021-01-22
>>> print(t)
12:20:34.915339
>>> d.strftime('%d/%m/%y')
'22/01/21'

>>> d.strftime('%d/%m/%y, %a')
'22/01/21, Fri'
>>> d.strftime('%d/%m/%y, %A')
'22/01/21, Friday'
>>> d.strftime('%d-%b-%y, %A')
'22-Jan-21, Friday'
>>> d.strftime('%d-%B-%y, %A')
'22-January-21, Friday'
>>> t.strftime('%H:%M:%S')
'12:20:34'
>>> t.strftime('%H:%M:%S, %p')
'12:20:34, PM'
>>> import calendar
>>> print(calendar.calendar(2021))
                                  2021

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

>>> calendar.month(2021,1)
'    January 2021\nMo Tu We Th Fr Sa Su\n             1  2  3\n 4  5  6  7  8  9 10\n11 12 13 14 15 16 17\n18 19 20 21 22 23 24\n25 26 27 28 29 30 31\n'
>>> print(calendar.month(2021,1))
    January 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

>>> 
====== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/chat_3.py =====
Enter your message : h
I don't understand
Enter your message : hi
Hello User
Enter your message : date
22/01/21, Fri
Enter your message : time
12/28/31, PM
Enter your message : bye
Bye User
>>> import os
>>> os.listdir()
['01-print.py', 'chat_1.py', 'chat_2.py', 'chat_3.py', 'continue_keyword.py', 'data_types.png', 'fib_series.py', 'guess_the_number.py', 'if_else_1.py', 'if_else_2.py', 'input_function.py', 'loop_1.py', 'loop_2.py', 'loop_3.py', 'loop_4.py', 'prime_2.py', 'prime_number.py', 'stone_paper_scissor.py', 'walrus.py', 'while_1.py']
>>> import glob
>>> glob.glob('*.mp3')
[]
>>> os.getcwd()
'C:\\Users\\acer\\OneDrive\\PythonRDE\\EC'
>>> os.chdir('C:\Users\acer\Music')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r'C:\Users\acer\Music')
>>> glob.glob('*.mp3')
['StreetFighter.mp3']
>>> os.listdir()
['attack.wav', 'desktop.ini', 'punch2.wav', 'StreetFighter.mp3', 'StreetFighter.ogg', 'theme.ogg', 've_music.wav']
>>> import random
>>> songs = os.listdir()
>>> s = random.choice(songs)
>>> os.startfile(s)
>>> 
>>> 
>>> import webbrowser
>>> webbrowser.open('facebook.com')
True
>>> 