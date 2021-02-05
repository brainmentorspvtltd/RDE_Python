Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> sayHello()
Hello User
>>> sayHello
<function sayHello at 0x000001B8CE9FC280>
>>> def sayBye():
	print("Bye User")

	
>>> greet = [sayHello(), sayBye()]
Hello User
Bye User
>>> greet
[None, None]
>>> greet = [sayHello, sayBye]
>>> greet
[<function sayHello at 0x000001B8CE9FC280>, <function sayBye at 0x000001B8CEA691F0>]
>>> greet[0]
<function sayHello at 0x000001B8CE9FC280>
>>> greet[1]
<function sayBye at 0x000001B8CEA691F0>
>>> greet[0]()
Hello User
>>> def sayHello(name):
	return "Hello " + name

>>> sayHello('Ravi')
'Hello Ravi'
>>> greet = sayHello('Ravi')
>>> greet
'Hello Ravi'
>>> def sayHello(name):
	print("Hello " + name)

	
>>> greet = sayHello('Ravi')
Hello Ravi
>>> greet
>>> def sayHello(name):
	return "Hello " + name

>>> greet = sayHello('Ravi')
>>> x = 8,7
>>> 