Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world"
>>> text = 'hello world'
>>> text = """hello world"""
>>> text[0]
'h'
>>> text[8]
'r'
>>> text[0:5]
'hello'
>>> text[0:9]
'hello wor'
>>> text[0:9:1]
'hello wor'
>>> text[0:9:2]
'hlowr'
>>> text[5]
' '
>>> text[0:9:9]
'h'
>>> text[9:0]
''
>>> text[9:0:-1]
'lrow olle'
>>> text[:]
'hello world'
>>> text[0:]
'hello world'
>>> text[:100]
'hello world'
>>> text[2:2]
''
>>> text[2:3]
'l'
>>> text[2:2]
''
>>> text[-1]
'd'
>>> text[-5]
'w'
>>> text[-1:-9]
''
>>> text[-1:-9:-1]
'dlrow ol'
>>> text[-9:-1]
'llo worl'
>>> text[-1:9]
''
>>> text[-1:9:-1]
'd'
>>> text[::-1]
'dlrow olleh'
>>> text[::-1] == text
False
>>> text = "nitin"
>>> text[::-1] == text
True
>>> text = "hello world"
>>> text[0]
'h'
>>> text[0] = 'i'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    text[0] = 'i'
TypeError: 'str' object does not support item assignment
>>> text = "hello world"
>>> text_1 = "hello world"
>>> text == text_1
True
>>> text is text_1
False
>>> x = 10
>>> y = 10
>>> x == y
True
>>> x is y
True
>>> id(x)
2407081011792
>>> id(y)
2407081011792
>>> id(text)
2407121356976
>>> id(text_1)
2407122067312
>>> text = "hello world"
>>> id(text)
2407116741616
>>> z = 10
>>> id(x)
2407081011792
>>> id(z)
2407081011792
>>> text_1 = "hello world"
>>> id(text_1)
2407089271408
>>> id('a')
2407081853488
>>> id('a')
2407081853488
>>> id('a')
2407081853488
>>> id('aman')
2407116741424
>>> id('aman')
2407116741424
>>> id('aman')
2407116741424
>>> id('hello')
2407122067312
>>> id('hello')
2407122067312
>>> id('hello')
2407122067312
>>> id('hello world')
2407122067248
>>> id('hello world')
2407116741424
>>> id('hello world')
2407121808112
>>> id('helloworld')
2407122067184
>>> id('helloworld')
2407122067184
>>> id('helloworld')
2407122067184
>>> text == text_1
True
>>> text is text_1
False
>>> 