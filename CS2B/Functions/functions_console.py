Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> msg = sayHello()
Hello User
>>> print(msg)
None
>>> def sayHello():
	return "Hello User"

>>> msg = sayHello()
>>> print(msg)
Hello User
>>> x = 10,1,1,1
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
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
  File "<pyshell#21>", line 1, in <module>
    counter()
  File "<pyshell#20>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	global x
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	global x
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x00000227ABE32350>
>>> count = counter()
>>> next(count)
1
>>> next(count)
2
>>> next(count)
3
>>> next(count)
4
>>> next(count)
5
>>> [i for i in range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (i for i in range(1,10))
<generator object <genexpr> at 0x00000227ABE32350>
>>> count = (i for i in range(1,10))
>>> next(count)
1
>>> next(count)
2
>>> for item in count:
	print(item)

	
3
4
5
6
7
8
9
>>> def sayHello():
	print("Hello User")

	
>>> sayHello()
Hello User
>>> sayHello
<function sayHello at 0x00000227ABEA9820>
>>> 