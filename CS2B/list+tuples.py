Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> numpy.array([2,3,1])
array([2, 3, 1])
>>> numpy.array([2,3,1,1.5,12.45])
array([ 2.  ,  3.  ,  1.  ,  1.5 , 12.45])
>>> numpy.array([2,3,1,1.5,12.45,'hello'])
array(['2', '3', '1', '1.5', '12.45', 'hello'], dtype='<U32')
>>> x = [2,3,4,1,4,'hi']
>>> x
[2, 3, 4, 1, 4, 'hi']
>>> x = []
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x[0] = 100
IndexError: list assignment index out of range
>>> x = list(range(1,10))
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[0] = 100
>>> x
[100, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = []
>>> x.append(10`0
	 
SyntaxError: invalid syntax
>>> x.append(10)
>>> x
[10]
>>> x.append(20)
>>> x
[10, 20]
>>> x = []
>>> for i in range(10,101,10):
	x.append(i)

	
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> x.append(11,22,33)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x.append(11,22,33)
TypeError: list.append() takes exactly one argument (3 given)
>>> x.append([11,22,33])
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, [11, 22, 33]]
>>> x.pop()
[11, 22, 33]
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> x + [11,22,33]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x * 2
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> x.extend([11,22,33])
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x.pop(2)
30
>>> x
[10, 20, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x.insert(2,30)
>>> x
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x[2] = 34
>>> x
[10, 20, 34, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x.remove(0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x.remove(0)
ValueError: list.remove(x): x not in list
>>> x.remove(34)
>>> x
[10, 20, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x.pop(0)
10
>>> x
[20, 40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> del x[0]
>>> x
[40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> sorted(x)
[11, 22, 33, 40, 50, 60, 70, 80, 90, 100]
>>> x
[40, 50, 60, 70, 80, 90, 100, 11, 22, 33]
>>> x.sort()
>>> x
[11, 22, 33, 40, 50, 60, 70, 80, 90, 100]
>>> x.sort(reverse=True)
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> x.index(70)
3
>>> x.count(11)
1
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> y = x
>>> x[0] = 1
>>> x
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> y
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> x == y
True
>>> x is y
True
>>> z = x.copy()
>>> x is z
False
>>> x[0] = 100
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> y
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> z
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> x.append([3,4,1,4])
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> y
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> z
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11]
>>> z = x.copy()
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> z
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> x[-1][0] = 300
>>> x
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> y
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> z
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> x[0] = 1
>>> x
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> y
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> z
[100, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> import copy
>>> z = copy.deepcopy(x)
>>> x
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> z
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> x[-1][0]
300
>>> x[-1][0] = 3
>>> x
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> z
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [300, 4, 1, 4]]
>>> x
[1, 90, 80, 70, 60, 50, 40, 33, 22, 11, [3, 4, 1, 4]]
>>> 50 in x
True
>>> 55 in x
False
>>> 55 not in x
True
>>> x = []
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [i**3 for i in range(1,11)]
>>> x
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> x = [i for i in range(1,11) if x % 2 == 0]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x = [i for i in range(1,11) if x % 2 == 0]
  File "<pyshell#99>", line 1, in <listcomp>
    x = [i for i in range(1,11) if x % 2 == 0]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> x = [i for i in range(1,11) if i % 2 == 0]
>>> x
[2, 4, 6, 8, 10]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # tuples
>>> x = 10
>>> x = 10,
>>> x
(10,)
>>> type(x)
<class 'tuple'>
>>> x = 10,12,14,16
>>> x = (10,12,14,16)
>>> data = ('Ram', 20, 'CS')
>>> name, age, branch = data
>>> name
'Ram'
>>> age
20
>>> branch
'CS'
>>> # packing & unpacking of data
>>> data[0]
'Ram'
>>> data[0] = 'laxman'
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    data[0] = 'laxman'
TypeError: 'tuple' object does not support item assignment
>>> del data[0]
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 