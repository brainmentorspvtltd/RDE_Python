Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [3,4,22,5,7,2,'hello',10.55]
>>> data = []
>>> data.append(5)
>>> data
[5]
>>> data.append(50)
>>> data
[5, 50]
>>> data.append(23)
>>> data
[5, 50, 23]
>>> data.append(12,21,5,7,2,3,4,5,7,8,9)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data.append(12,21,5,7,2,3,4,5,7,8,9)
TypeError: list.append() takes exactly one argument (11 given)
>>> data.append([12,21,5,7,2,3,4,5,7,8,9])
>>> data
[5, 50, 23, [12, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]]
>>> data.pop()
[12, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]
>>> data
[5, 50, 23]
>>> data.extend([12, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9])
>>> data
[5, 50, 23, 12, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]
>>> data.pop(2)
23
>>> data
[5, 50, 12, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]
>>> data.insert(3,22)
>>> data
[5, 50, 12, 22, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]
>>> data.remove(1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data.remove(1)
ValueError: list.remove(x): x not in list
>>> data.remove(50)
>>> data
[5, 12, 22, 21, 5, 7, 2, 3, 4, 5, 7, 8, 9]
>>> data.count(5)
3
>>> data.index(5)
0
>>> data.index(5,1)
4
>>> sorted(data)
[2, 3, 4, 5, 5, 5, 7, 7, 8, 9, 12, 21, 22]
>>> data.sort()
>>> data
[2, 3, 4, 5, 5, 5, 7, 7, 8, 9, 12, 21, 22]
>>> data.sort(reverse=True)
>>> data
[22, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> for i in range(len(data)):
	if data[i] == 4:
		print("Found 4 at",i)

		
Found 4 at 10
>>> 4 in data
True
>>> 100 in data
False
>>> data[0]
22
>>> data[0:5]
[22, 21, 12, 9, 8]
>>> data[-1]
2
>>> data[::-1]
[2, 3, 4, 5, 5, 5, 7, 7, 8, 9, 12, 21, 22]
>>> data_1 = data
>>> data_1 == data
True
>>> data_1 is data
True
>>> data_1[0]
22
>>> data[0]
22
>>> data_1[0] = 100
>>> data_1
[100, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> data
[100, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> data[:]
[100, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> data_2 = data[:]
>>> data is data_2
False
>>> data[0] = 200
>>> data
[200, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> data_2
[100, 21, 12, 9, 8, 7, 7, 5, 5, 5, 4, 3, 2]
>>> data = [[100, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 2]
>>> data[0]
[100, 21, 12, 9, 8]
>>> data[0][0]
100
>>> data_1 = data
>>> data_2 = data[:]
>>> data_1[-1] = 20
>>> data
[[100, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 20]
>>> data_2
[[100, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 2]
>>> data[0][0] = 500
>>> data_1
[[500, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 20]
>>> data_2
[[500, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 2]
>>> data_1 = data
>>> data_2 = data[:]
>>> data[-1] = 100
>>> data
[[500, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 100]
>>> data_2
[[500, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 20]
>>> data[0][0] = 5
>>> data_2
[[5, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 20]
>>> import copy
>>> data_3 = copy.deepcopy(data)
>>> data[0][0] = 50
>>> data
[[50, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 100]
>>> data_1
[[50, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 100]
>>> data_2
[[50, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 20]
>>> data_3
[[5, 21, 12, 9, 8], 7, 7, 5, 5, 5, 4, 3, 100]
>>> data = []
>>> for i in range(50):
	data.append(i)

	
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> data = [i for i in range(50)]
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> data = [i for i in range(50) if i % 2 == 0]
>>> data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data = [(i,j) for i in range(50) for j in range(5) if i == j]
>>> data
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
>>> 