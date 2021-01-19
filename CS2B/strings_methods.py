Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = 'hello world, this is python programming'
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.find('o')
4
>>> text.count('o')
4
>>> text.find('o')
4
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.index('o')
4
>>> text.index('o', 5)
7
>>> text.index('o', 8)
25
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rfind('o')
30
>>> text
'hello world, this is python programming'
>>> text.rindex('o')
30
>>> text.center(5)
'hello world, this is python programming'
>>> text.center(20)
'hello world, this is python programming'
>>> len(text)
39
>>> text.center(38)
'hello world, this is python programming'
>>> text.center(39)
'hello world, this is python programming'
>>> text.center(40)
'hello world, this is python programming '
>>> text.center(41)
' hello world, this is python programming '
>>> text.center(51)
'      hello world, this is python programming      '
>>> text.center(51,'*')
'******hello world, this is python programming******'
>>> text = text.center(51,'*')
>>> text
'******hello world, this is python programming******'
>>> text.strip()
'******hello world, this is python programming******'
>>> text.strip('*')
'hello world, this is python programming'
>>> text
'******hello world, this is python programming******'
>>> text.lstrip()
'******hello world, this is python programming******'
>>> text.lstrip('*')
'hello world, this is python programming******'
>>> text.rstrip('*')
'******hello world, this is python programming'
>>> text.replace('*','-')
'------hello world, this is python programming------'
>>> text
'******hello world, this is python programming******'
>>> text.endswith('?')
False
>>> text.endswith('*')
True
>>> text.startswith('&')
False
>>> text.isalnum()
False
>>> text.isspace()
False
>>> text.islower()
True
>>> text.split()
['******hello', 'world,', 'this', 'is', 'python', 'programming******']
>>> text = text.strip('*')
>>> text
'hello world, this is python programming'
>>> text.split()
['hello', 'world,', 'this', 'is', 'python', 'programming']
>>> text = text.split()
>>> text
['hello', 'world,', 'this', 'is', 'python', 'programming']
>>> ' '.join(text)
'hello world, this is python programming'
>>> ','.join(text)
'hello,world,,this,is,python,programming'
>>> '--'.join(text)
'hello--world,--this--is--python--programming'
>>> 