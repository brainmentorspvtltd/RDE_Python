Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> x = list()
>>> x = [4,3,5,6,7,8,'hi']
>>> x[0]
4
>>> x[0:4]
[4, 3, 5, 6]
>>> x[-1]
'hi'
>>> x[::-1]
['hi', 8, 7, 6, 5, 3, 4]
>>> x[-1] = 10
>>> x
[4, 3, 5, 6, 7, 8, 10]
>>> #LIFO - Last In First Out
>>> x.append(5)
>>> x
[4, 3, 5, 6, 7, 8, 10, 5]
>>> x.pop()
5
>>> x
[4, 3, 5, 6, 7, 8, 10]
>>> x.append(5,6,4,6,7)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x.append(5,6,4,6,7)
TypeError: list.append() takes exactly one argument (5 given)
>>> x.append([5,6,4,6,7])
>>> x
[4, 3, 5, 6, 7, 8, 10, [5, 6, 4, 6, 7]]
>>> x.pop()
[5, 6, 4, 6, 7]
>>> x
[4, 3, 5, 6, 7, 8, 10]
>>> x.extend([5,6,4,6,7])
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7]
>>> x + [2,34,4,6,7]
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7, 2, 34, 4, 6, 7]
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7]
>>> x * 2
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7, 4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7]
>>> import numpy as np
>>> np.mean(x)
5.916666666666667
>>> x1 = np.array(x)
>>> x1
array([ 4,  3,  5,  6,  7,  8, 10,  5,  6,  4,  6,  7])
>>> x1 * 2
array([ 8,  6, 10, 12, 14, 16, 20, 10, 12,  8, 12, 14])
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 6, 7]
>>> x.pop(-2)
6
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 7]
>>> x.pop(3)
6
>>> x
[4, 3, 5, 7, 8, 10, 5, 6, 4, 7]
>>> x.insert(3,6)
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 7]
>>> x.count(5)
2
>>> x.index(6)
3
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 7]
>>> sorted(x)
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 10]
>>> x
[4, 3, 5, 6, 7, 8, 10, 5, 6, 4, 7]
>>> x.sort()
>>> x
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 10]
>>> x.sort(reverse=True)
>>> x
[10, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3]
>>> x.reverse()
>>> x
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 10]
>>> x.remove(10)
>>> x
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> x.remove(0)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x.remove(0)
ValueError: list.remove(x): x not in list
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> y = x.copy()
>>> x
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> y
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> x == y
True
>>> x[0] = 100
>>> x
[100, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> y
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> z = x
>>> x
[100, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> y
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> z
[100, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> x == z
True
>>> x[0] = 10
>>> x
[10, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> y
[3, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> z
[10, 4, 4, 5, 5, 6, 6, 7, 7, 8]
>>> x.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for sort()
>>> x.sort(reverse = True)
>>> x
[10, 8, 7, 7, 6, 6, 5, 5, 4, 4]
>>> x = "hello"
>>> x.replace('h','x')
'xello'
>>> x
'hello'
>>> x = x.replace('h','x')
>>> x
'xello'
>>> 