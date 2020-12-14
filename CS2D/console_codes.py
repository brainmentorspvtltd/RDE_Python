Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:\Users\acer\Desktop\PythonRDE\CS2D\walrus.py ===========

Addition is 15
Subtraction is -5
Division is 0.5
Multiplication is 50

>>> x = 5
>>> y = 7
>>> 
>>> z = x + y
>>> print(z)
12
>>> print(z := x + y)
12
>>> z
12
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name : Ravi
Hello Ravi
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name : Ravi
Hello Ravi
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name : Ravi
Hello Ravi
Enter first number : 5
Enter second number : 5
Sum is 55
>>> '5' + '5'
'55'
>>> x
'5'
>>> type(x)
<class 'str'>
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name : Ravi
Hello Ravi
Enter first number : 12
Enter second number : 2
Sum is 14
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name :       
Hello       
Enter first number :  
Traceback (most recent call last):
  File "C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py", line 10, in <module>
    x = int(input("Enter first number : "))
ValueError: invalid literal for int() with base 10: ' '
>>> 
======== RESTART: C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py =======
Enter your name : 5 7
Hello 5 7
Enter first number : 
Traceback (most recent call last):
  File "C:/Users/acer/Desktop/PythonRDE/CS2D/input_function.py", line 10, in <module>
    x = int(input("Enter first number : "))
ValueError: invalid literal for int() with base 10: ''
>>> x = 'ौैसलरकिजीहिपेदेजीरदगिरदिेद्िदे्सिदे'
>>> x/enumerat
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x/enumerat
NameError: name 'enumerat' is not defined
>>> x.encode()
b'\xe0\xa5\x8c\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa4\xb2\xe0\xa4\xb0\xe0\xa4\x95\xe0\xa4\xbf\xe0\xa4\x9c\xe0\xa5\x80\xe0\xa4\xb9\xe0\xa4\xbf\xe0\xa4\xaa\xe0\xa5\x87\xe0\xa4\xa6\xe0\xa5\x87\xe0\xa4\x9c\xe0\xa5\x80\xe0\xa4\xb0\xe0\xa4\xa6\xe0\xa4\x97\xe0\xa4\xbf\xe0\xa4\xb0\xe0\xa4\xa6\xe0\xa4\xbf\xe0\xa5\x87\xe0\xa4\xa6\xe0\xa5\x8d\xe0\xa4\xbf\xe0\xa4\xa6\xe0\xa5\x87\xe0\xa5\x8d\xe0\xa4\xb8\xe0\xa4\xbf\xe0\xa4\xa6\xe0\xa5\x87'
>>> x
'ौैसलरकिजीहिपेदेजीरदगिरदिेद्िदे्सिदे'
>>> y = x.encode()
>>> type(y)
<class 'bytes'>
>>> x = 'hello world'
>>> x[0]
'h'
>>> x[0] = 'y'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x[0] = 'y'
TypeError: 'str' object does not support item assignment
>>> x = [43,5,6,8,6]
>>> x[0]
43
>>> x[0] = 4
>>> x
[4, 5, 6, 8, 6]
>>> s ** 7
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s ** 7
NameError: name 's' is not defined
>>> 2 ** 7
128
>>> x = 10
>>> type(x)
<class 'int'>
>>> id(10)
2809430239824
>>> x = 10
>>> y = 10
>>> z = x
>>> id(10)
2809430239824
>>> id(x)
2809430239824
>>> id(y)
2809430239824
>>> id(z)
2809430239824
>>> import sys
>>> sys.getsizeof(1)
28
>>> sys.getsizeof(1000)
28
>>> sys.getsizeof(10000000)
28
>>> sys.getsizeof(1000000000)
28
>>> sys.getsizeof(10000000000)
32
>>> sys.getsizeof(1000000000000000000)
32
>>> sys.getsizeof(0)
24
>>> sys.getsizeof('')
49
>>> sys.getsizeof('h')
50
>>> sys.getsizeof('he')
51
>>> sys.getsizeof('hel')
52
>>> 