Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = (4,3,5,3)
>>> type(x)
<class 'tuple'>
>>> x = (3,4,6,1,'hi',10.55)
>>> x.count(3)
1
>>> x.index(3)
0
>>> x[0]
3
>>> x[0] = 30
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[0] = 30
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = 10,21,3,45,6,7,5,3
>>> type(x)
<class 'tuple'>
>>> data = name, age, salary = 'Ram', 45, 56000
>>> name
'Ram'
>>> age
45
>>> salary
56000
>>> data
('Ram', 45, 56000)
>>> data
('Ram', 45, 56000)
>>> name, age, salary = data
>>> name
'Ram'
>>> age
45
>>> salary
56000
>>> data = [(101,'Ram','CS'),(102,'Aman','EC'),(103,'Shyam','ME')]
>>> data[0]
(101, 'Ram', 'CS')
>>> data_1 = data[0]
>>> for i in range(len(data_1))"
SyntaxError: EOL while scanning string literal
>>> for i in range(len(data_1)):
	print(data_1[i])

	
101
Ram
CS
>>> data_1[0]
101
>>> data_1[1]
'Ram'
>>> data_1[2]
'CS'
>>> for item in data_1:
	print(item)

	
101
Ram
CS
>>> for i in range(len(data_1)):
	print(data_1[i])

	
101
Ram
CS
>>> enumerate(data_1)
<enumerate object at 0x0000026CCC6DFB00>
>>> for i, item in enumerate(data_1):
	print(i, item)

	
0 101
1 Ram
2 CS
>>> [i for i in range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (i for i in range(1,10))
<generator object <genexpr> at 0x0000026CCE744DD0>
>>> 