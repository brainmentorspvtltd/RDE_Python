Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = 'hello python'
>>> ord
<built-in function ord>
>>> chr
<built-in function chr>
>>> chr(67)
'C'
>>> ord(97)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ord(97)
TypeError: ord() expected string of length 1, but int found
>>> ord('a')
97
>>> bin(97)
'0b1100001'
>>> len(text)
12
>>> text
'hello python'
>>> text[0]
'h'
>>> text[1]
'e'
>>> text[-1]
'n'
>>> text[-2]
'o'
>>> text
'hello python'
>>> text[0:4]
'hell'
>>> text[4]
'o'
>>> text[1:10]
'ello pyth'
>>> #text[index (start) : position (stop) : step(defualt=1)]
>>> text[0:10:2]
'hlopt'
>>> text
'hello python'
>>> text[10:0]
''
>>> text[10:0:-1]
'ohtyp olle'
>>> text[10::-1]
'ohtyp olleh'
>>> text[:]
'hello python'
>>> text[0:]
'hello python'
>>> text[:8]
'hello py'
>>> text[:80]
'hello python'
>>> text[::-1]
'nohtyp olleh'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'nohtyp ol'
>>> text[-10:-1]
'llo pytho'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello python'
>>> text.upper()
'HELLO PYTHON'
>>> text.capitalize()
'Hello python'
>>> text.title()
'Hello Python'
>>> text.swapcase()
'HELLO PYTHON'
>>> text.count('o')
2
>>> text.index('o')
4
>>> text.index('o',5)
10
>>> text.index('o',11)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    text.index('o',11)
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('o',5)
10
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.find('o',11)
-1
>>> text.rfind('o')
10
>>> text.find('o')
4
>>> text.index('o')
4
>>> text.rindex('o')
10
>>> text.split()
['hello', 'python']
>>> #tokenization
>>> text = "hello python, hello java, hello php"
>>> text.split()
['hello', 'python,', 'hello', 'java,', 'hello', 'php']
>>> text.split(',')
['hello python', ' hello java', ' hello php']
>>> data = ['hello python', ' hello java', ' hello php']
>>> ' '.join(data)
'hello python  hello java  hello php'
>>> ','.join(data)
'hello python, hello java, hello php'
>>> text
'hello python, hello java, hello php'
>>> text = '    hello python, hello java, hello php     '
>>> text.strip()
'hello python, hello java, hello php'
>>> text = '    hello python, hello java, hello php*****'
>>> text.strip()
'hello python, hello java, hello php*****'
>>> text.strip('*')
'    hello python, hello java, hello php'
>>> text.lstrip()
'hello python, hello java, hello php*****'
>>> text.rstrip()
'    hello python, hello java, hello php*****'
>>> text.rstrip('*')
'    hello python, hello java, hello php'
>>> text = text.rstrip('*')
>>> text.lstrip()
'hello python, hello java, hello php'
>>> text.center(10)
'    hello python, hello java, hello php'
>>> text
'    hello python, hello java, hello php'
>>> text = text.lstrip()
>>> text
'hello python, hello java, hello php'
>>> text.center(10)
'hello python, hello java, hello php'
>>> text.center(20)
'hello python, hello java, hello php'
>>> text.center(30)
'hello python, hello java, hello php'
>>> len(text)
35
>>> text.center(36)
'hello python, hello java, hello php '
>>> text.center(37)
' hello python, hello java, hello php '
>>> text.center(47)
'      hello python, hello java, hello php      '
>>> text.center(47,'*')
'******hello python, hello java, hello php******'
>>> text.startswith('A')
False
>>> text.startswith('h')
True
>>> text.endswith('?')
False
>>> text.endswith('.')
False
>>> text.endswith('p')
True
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.istitle()
False
>>> 