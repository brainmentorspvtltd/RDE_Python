Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> counter()
1
>>> x = 0
>>> def counter():
	while True:
		x += 1
		return x

	
>>> counter()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    counter()
  File "<pyshell#11>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	while True:
		return x + 1

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter
<function counter at 0x0000026B82947280>
>>> counter()
<generator object counter at 0x0000026B82954F90>
>>> next([3,4,5,2,2,5])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    next([3,4,5,2,2,5])
TypeError: 'list' object is not an iterator
>>> next(counter())
1
>>> next(counter())
1
>>> counter()
<generator object counter at 0x0000026B82954F90>
>>> count = counter()
>>> next(count)
1
>>> next(count)
2
>>> next(count)
3
>>> next(count)
4
>>> [i for i in range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (i for i in range(1,10))
<generator object <genexpr> at 0x0000026B82954F90>
>>> obj = (i for i in range(1,10))
>>> obj
<generator object <genexpr> at 0x0000026B829610B0>
>>> next(obj)
1
>>> next(obj)
2
>>> next(obj)
3
>>> next(obj)
4
>>> for i in obj:
	print(i)

	
5
6
7
8
9
>>> def func_1():
	return 1
	return 2
	return 3

>>> func_1()
1
>>> def func_1():
	yield 1
	yield 2
	yield 3

	
>>> func_1()
<generator object func_1 at 0x0000026B82954F90>
>>> x = func_1()
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    next(x)
StopIteration
>>> def outer():
	msg = "Hello"

	
>>> outer()
>>> print(msg)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(msg)
NameError: name 'msg' is not defined
>>> def outer():
	msg = "Hello"
	return msg

>>> outer()
'Hello'
>>> msg = outer()
>>> print(msg)
Hello
>>> def greet():
	def hello():
		msg = "Hello"
		return msg
	def bye():
		msg = "Bye"
		return msg

	
>>> greet()
>>> def greet():
	def hello():
		msg = "Hello"
		return msg
	def bye():
		msg = "Bye"
		return msg
	hello()
	bye()

	
>>> greet()
>>> def greet():
	def hello():
		msg = "Hello"
		print(msg)
	def bye():
		msg = "Bye"
		print(msg)
	hello()
	bye()

	
>>> greet()
Hello
Bye
>>> def greet():
	def hello():
		msg = "Hello"
		print(msg)
	def bye():
		msg = "Bye"
		print(msg)
	return hello()

>>> greet()
Hello
>>> hello greet()
SyntaxError: invalid syntax
>>> hello = greet()
Hello
>>> print(hello)
None
>>> def greet():
	def hello():
		msg = "Hello"
		print(msg)
	def bye():
		msg = "Bye"
		print(msg)
	return hello

>>> hello = greet()
>>> hello()
Hello
>>> hello
<function greet.<locals>.hello at 0x0000026B82947940>
>>> hey = greet()
>>> hey()
Hello
>>> def greet():
	def hello():
		msg = "Hello"
		print(msg)
	def bye():
		msg = "Bye"
		print(msg)
	return hello, bye

>>> greet()
(<function greet.<locals>.hello at 0x0000026B82947A60>, <function greet.<locals>.bye at 0x0000026B82947C10>)
>>> greet()[0]
<function greet.<locals>.hello at 0x0000026B82947CA0>
>>> greet()[0]()
Hello
>>> greet()[1]()
Bye
>>> def hello():
	print("Hello")

	
>>> hello
<function hello at 0x0000026B82947C10>
>>> hello()
Hello
>>> 