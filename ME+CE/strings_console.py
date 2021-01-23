Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> text = "hello world, this is python programming"
>>> text = 'hello world, this is python programming'
>>> text = '''hello world, this is python programming'''
>>> text = """hello world, this is python programming"""
>>> text = """hello world, this is python programming"""
>>> text[0:4]
'hell'
>>> text[0:10]
'hello worl'
>>> text[0:10:2]
'hlowr'
>>> text[0:10:1]
'hello worl'
>>> text[0:30:3]
'hlwl iiph '
>>> text[0]
'h'
>>> text[0]
'h'
>>> text[7]
'o'
>>> #text[index/start : pos/stop = index - 1]
>>> text
'hello world, this is python programming'
>>> text[0:30]
'hello world, this is python pr'
>>> text[0:30:1]
'hello world, this is python pr'
>>> text[0:30:2]
'hlowrd hsi yhnp'
>>> text[10:0]
''
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[:]
'hello world, this is python programming'
>>> text[10:]
'd, this is python programming'
>>> text[:30]
'hello world, this is python pr'
>>> text[::-1]
'gnimmargorp nohtyp si siht ,dlrow olleh'
>>> text
'hello world, this is python programming'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.lower()
'hello world, this is python programming'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.count('o')
4
>>> text.index('o')
4
>>> text.index('o', 5)
7
>>> text.index('o', 8)
25
>>> text.index('o', 26)
30
>>> text.rindex('o')
30
>>> text.count('o', 10,20)
0
>>> text.find('o')
4
>>> text.find('o', 5)
7
>>> text.find('o', 8)
25
>>> text.find('z')
-1
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('pro')
28
>>> text
'hello world, this is python programming'
>>> text.replace('hello', 'bye')
'bye world, this is python programming'
>>> text.isalnum()
False
>>> text.isascii()
True
>>> text.isdigit()
False
>>> text.isupper()
False
>>> text.islower()
True
>>> text.isspace()
False
>>> text.center(10)
'hello world, this is python programming'
>>> text.center(20)
'hello world, this is python programming'
>>> text.center(30)
'hello world, this is python programming'
>>> len(text)
39
>>> text.center(39)
'hello world, this is python programming'
>>> text.center(40)
'hello world, this is python programming '
>>> text.center(41)
' hello world, this is python programming '
>>> text.center(51)
'      hello world, this is python programming      '
>>> text.center(51, '*')
'******hello world, this is python programming******'
>>> text = text.center(51)
>>> text
'      hello world, this is python programming      '
>>> text.strip()
'hello world, this is python programming'
>>> text.lstrip()
'hello world, this is python programming      '
>>> text.rstrip()
'      hello world, this is python programming'
>>> text.strip()
'hello world, this is python programming'
>>> text = text.center(51, '*')
>>> text
'      hello world, this is python programming      '
>>> text = text.center(51,'*')
>>> text
'      hello world, this is python programming      '
>>> text.center(51,'*')
'      hello world, this is python programming      '
>>> text = text.strip()
>>> text = text.center(51,'*')
>>> text
'******hello world, this is python programming******'
>>> text.strip()
'******hello world, this is python programming******'
>>> text.strip('*')
'hello world, this is python programming'
>>> text
'******hello world, this is python programming******'
>>> text = text.strip()
>>> text
'******hello world, this is python programming******'
>>> text = text.strip('*')
>>> text
'hello world, this is python programming'
>>> text = text.center(51)
>>> tet
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    tet
NameError: name 'tet' is not defined
>>> text
'      hello world, this is python programming      '
>>> text.strip(' ')
'hello world, this is python programming'
>>> text.startswith('a')
False
>>> text.startswith('a',10)
False
>>> text.endswith('?')
False
>>> text
'      hello world, this is python programming      '
>>> text.endswith(' ')
True
>>> 