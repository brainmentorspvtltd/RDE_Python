Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:\Users\acer\OneDrive\PythonRDE\CS2B\chat_1.py ====
Enter your name : x
Welcome x
Enter your message : bye
Bye x, Take Care...
>>> import webbrowser
>>> webbrowser.open('google.com')
True
>>> webbrowser.open('facebook.com')
True
>>> msg = 'open facebook'
>>> msg.split()
['open', 'facebook']
>>> msg.split()[-1]
'facebook'
>>> web = msg.split()[-1]
>>> webbrowser.open(f'{web}.com')
True
>>> 