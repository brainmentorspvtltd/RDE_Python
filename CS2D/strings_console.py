Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is python programming..."
>>> text[0]
'h'
>>> text[-1]
'.'
>>> len(text)
42
>>> text[0:4]
'hell'
>>> text[0:1]
'h'
>>> text[0:20]
'hello world, this is'
>>> text[:]
'hello world, this is python programming...'
>>> text[0:]
'hello world, this is python programming...'
>>> text[5:]
' world, this is python programming...'
>>> text[:100]
'hello world, this is python programming...'
>>> text[0:20:1]
'hello world, this is'
>>> text[0:20:2]
'hlowrd hsi'
>>> text[0:20:3]
'hlwl ii'
>>> text[0::3]
'hlwl iiph oai.'
>>> text[::3]
'hlwl iiph oai.'
>>> text[10:1]
''
>>> text[10:1:-1]
'dlrow oll'
>>> range(1,10)
range(1, 10)
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> text[10:0]
''
>>> text[10:0:-1]
'dlrow olle'
>>> text[10:-1:-1]
''
>>> text[10::-1]
'dlrow olleh'
>>> tex[::-1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tex[::-1]
NameError: name 'tex' is not defined
>>> text[::-1]
'...gnimmargorp nohtyp si siht ,dlrow olleh'
>>> x = 'nitin'
>>> x[:] == x[::-1]
True
>>> text[-1]
'.'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'...gnimma'
>>> tex[-10:-1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tex[-10:-1]
NameError: name 'tex' is not defined
>>> text[-10:-1]
'ramming..'
>>> range
<class 'range'>
>>> input
<built-in function input>
>>> str.format
<method 'format' of 'str' objects>
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming...'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING...'
>>> text.capitalize()
'Hello world, this is python programming...'
>>> text.title()
'Hello World, This Is Python Programming...'
>>> text.index('o')
4
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('z')
-1
>>> text.count('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> text.find('o',31)
-1
>>> text.rfind('o')
30
>>> text.rfind('o',29)
30
>>> text.rfind('o',29,20)
-1
>>> text.rfind('o',29,10)
-1
>>> text.rfind('o',20,29)
25
>>> text.split()
['hello', 'world,', 'this', 'is', 'python', 'programming...']
>>> text.split(',')
['hello world', ' this is python programming...']
>>> text.split()
['hello', 'world,', 'this', 'is', 'python', 'programming...']
>>> text.split('is')
['hello world, th', ' ', ' python programming...']
>>> text.split(' is')
['hello world, this', ' python programming...']
>>> x = text.split()
>>> x
['hello', 'world,', 'this', 'is', 'python', 'programming...']
>>> ' '.join(x)
'hello world, this is python programming...'
>>> '-'.join(x)
'hello-world,-this-is-python-programming...'
>>> msg = ' '.join(x)
>>> msg
'hello world, this is python programming...'
>>> msg = '    hello world, this is python programming     '
>>> msg.strip()
'hello world, this is python programming'
>>> msg = '    hello world, this is python programming------'
>>> msg.strip()
'hello world, this is python programming------'
>>> msg.lstrip()
'hello world, this is python programming------'
>>> msg.rstrip('-')
'    hello world, this is python programming'
>>> msg = msg.lstrip()
>>> msg = msg.rstrip('-')
>>> msg
'hello world, this is python programming'
>>> 