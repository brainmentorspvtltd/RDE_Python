Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> y = 20
>>> z = x + y
>>> z
30
>>> 
=========== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py ==========
11
>>> 
=========== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py ==========
11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is-11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of a and b is c
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum is 11
>>> name = 'Ram'
>>> sal = 35000
>>> msg = 'Hello ' + name + " your salary is " + sal
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    msg = 'Hello ' + name + " your salary is " + sal
TypeError: can only concatenate str (not "int") to str
>>> msg = "Hello {}, your salary is {}".format(name,sal)
>>> msg
'Hello Ram, your salary is 35000'
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum of 5 and 6 is 11
>>> 
= RESTART: C:/Users/acer/Desktop/PythonRDE/CS2C/01-print.py
11
Sum is,11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum is 11
Sum of 5 and 6 is 11
Sum of 5 and 6 is 11
Sum of 5 and 6 is 11
>>> import os
>>> path = 'C:\Users\acer\Desktop\PythonDemo\Game\StreetFighter\snd'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = r'C:\Users\acer\Desktop\PythonDemo\Game\StreetFighter\snd'
>>> path
'C:\\Users\\acer\\Desktop\\PythonDemo\\Game\\StreetFighter\\snd'
>>> os.startfile(path+'\\'+'theme.ogg')
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(40):
	t.forward(5 * i)
	t.left(45 * i)

	
Traceback (most recent call last):
  File "<pyshell#32>", line 3, in <module>
    t.left(45 * i)
  File "C:\Python39\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Python39\lib\turtle.py", line 3277, in _rotate
    self._update()
  File "C:\Python39\lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python39\lib\turtle.py", line 567, in _delay
    self.cv.after(delay)
  File "C:\Python39\lib\tkinter\__init__.py", line 801, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> t.reset()
>>> for i in range(40):
	t.forward(5 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(40):
	t.circle(5 * i)
	t.left(45)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    t.circle(5 * i)
  File "C:\Python39\lib\turtle.py", line 1994, in circle
    self._rotate(w)
  File "C:\Python39\lib\turtle.py", line 3279, in _rotate
    self._update()
  File "C:\Python39\lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python39\lib\turtle.py", line 567, in _delay
    self.cv.after(delay)
  File "C:\Python39\lib\tkinter\__init__.py", line 801, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> t.reset()
>>> t.speed(0)
>>> for i in range(40):
	t.circle(5 * i)
	t.left(45)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(80):
	t.circle(5 * i)
	t.left(90)

	
>>> 