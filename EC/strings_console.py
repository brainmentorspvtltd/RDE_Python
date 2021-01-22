Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is python programming"
>>> type(text)
<class 'str'>
>>> text[0]
'h'
>>> text[0:5]
'hello'
>>> text[10:30]
'd, this is python pr'
>>> text[0:30:2]
'hlowrd hsi yhnp'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-1:-10]
''
>>> text[1:10]
'ello worl'
>>> text[10:1:-1]
'dlrow oll'
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> text[:]
'hello world, this is python programming'
>>> text[0:]
'hello world, this is python programming'
>>> text[:10]
'hello worl'
>>> text[::-1]
'gnimmargorp nohtyp si siht ,dlrow olleh'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
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
>>> text.count('o')
4
>>> text.count('i')
3
>>> text.count('m')
2
>>> text.count('o' 10, 30)
SyntaxError: invalid syntax
>>> text.count('o', 10, 30)
1
>>> len(text)
39
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.find('o')
4
>>> text.find('o',8)
25
>>> text.find('o',5)
7
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.isalnum()
False
>>> text.isascii()
True
>>> text.islower()
True
>>> text.isupper()
False
>>> text.endswith('?')
False
>>> text.endswith('.')
False
>>> 