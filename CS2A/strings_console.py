Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world"
>>> text[0]
'h'
>>> text[10]
'd'
>>> text[-1]
'd'
>>> text[0:4]
'hell'
>>> text[0:10]
'hello worl'
>>> text[10:1]
''
>>> #text[start=0:end=10:step=1]
>>> text[0:10:1]
'hello worl'
>>> text[0:10:2]
'hlowr'
>>> text[10:1:-1]
'dlrow oll'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'dlrow oll'
>>> text[:]
'hello world'
>>> text[0:]
'hello world'
>>> text[:7]
'hello w'
>>> text[0:100]
'hello world'
>>> text[::]
'hello world'
>>> text[::-1]
'dlrow olleh'
>>> text[-1:10]
''
>>> text[-1:9]
''
>>> text[-1:8]
''
>>> text[-1:10:-1]
''
>>> text[-1:9:-1]
'd'
>>> text[10:1]
''
>>> text[10:1:-1]
'dlrow oll'
>>> text[-1:9:-1]
'd'
>>> text]
SyntaxError: unmatched ']'
>>> text[9:3:-1]
'lrow o'
>>> len(text)
11
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.upper()
'HELLO WORLD'
>>> text.lower()
'hello world'
>>> text.capitalize()
'Hello world'
>>> text.title()
'Hello World'
>>> text.count('o')
2
>>> text.count(' ')
1
>>> text.replace('h','x')
'xello world'
>>> text
'hello world'
>>> text.find('o')
4
>>> text.find('o',0)
4
>>> text.find('o',5)
7
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.isalpha()
False
>>> text.islower()
True
>>> 