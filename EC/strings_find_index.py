Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = 'hello world'
>>> start = 0
>>> char = 'o'
>>> text.count(char)
2
>>> x = text.count(char)
>>> for i in range(x):
	index = text.find(char, start)
	start = index + 1
	print(index)

	
4
7
>>> 