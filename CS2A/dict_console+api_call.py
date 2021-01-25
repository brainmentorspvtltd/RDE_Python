Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = 10,20,30,40
>>> x = (10,20,30,40)
>>> x[0]
10
>>> x[0:3]
(10, 20, 30)
>>> x.count(10)
1
>>> x.index(10)
0
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = 'Ramesh', 45, 56000
>>> #unpacking
>>> name, age, salary = data
>>> name
'Ramesh'
>>> age
45
>>> salary
56000
>>> name, age, salary, x = data
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name, age, salary, x = data
ValueError: not enough values to unpack (expected 4, got 3)
>>> name, age, = data
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name, age, = data
ValueError: too many values to unpack (expected 2)
>>> name, *age = data
>>> name
'Ramesh'
>>> age
[45, 56000]
>>> data = {}
>>> type(data)
<class 'dict'>
>>> data = dict()
>>> data = {'name':'Ramesh', 'college':'RDEC', 'year':2}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ramesh'
>>> data['college']
'RDEC'
>>> data['name'] = 'Raman'
>>> data
{'name': 'Raman', 'college': 'RDEC', 'year': 2}
>>> data['sem'] = 4
>>> data
{'name': 'Raman', 'college': 'RDEC', 'year': 2, 'sem': 4}
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['name', 'college', 'year', 'sem'])
>>> data.values()
dict_values(['Raman', 'RDEC', 2, 4])
>>> data.items()
dict_items([('name', 'Raman'), ('college', 'RDEC'), ('year', 2), ('sem', 4)])
>>> data['hobby']
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    data['hobby']
KeyError: 'hobby'
>>> data.get('hobby')
>>> data.get('hobby', 'Not available')
'Not available'
>>> data.get('year', 'Not available')
2
>>> data.setdefault('hobby')
>>> data
{'name': 'Raman', 'college': 'RDEC', 'year': 2, 'sem': 4, 'hobby': None}
>>> data['hobby'] = 'cricket'
>>> data
{'name': 'Raman', 'college': 'RDEC', 'year': 2, 'sem': 4, 'hobby': 'cricket'}
>>> data.pop()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.pop('year')
2
>>> data
{'name': 'Raman', 'college': 'RDEC', 'sem': 4, 'hobby': 'cricket'}
>>> data.popitem()
('hobby', 'cricket')
>>> data
{'name': 'Raman', 'college': 'RDEC', 'sem': 4}
>>> data.update({'year':2, 'hobby':'cricket'})
>>> data
{'name': 'Raman', 'college': 'RDEC', 'sem': 4, 'year': 2, 'hobby': 'cricket'}
>>> data.update({'year':4, 'hobby':'football'})
>>> data
{'name': 'Raman', 'college': 'RDEC', 'sem': 4, 'year': 4, 'hobby': 'football'}
>>> for i in range(len(data)):
	print(data[i])

	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print(data[i])
KeyError: 0
>>> for key in data:
	print(key)

	
name
college
sem
year
hobby
>>> for key in data:
	print(data[key])

	
Raman
RDEC
4
4
football
>>> for key in data:
	print(key,":",data[key])

	
name : Raman
college : RDEC
sem : 4
year : 4
hobby : football
>>> [i for i in range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [i for i in range(1,10) if i % 2 == 0]
[2, 4, 6, 8]
>>> (i for i in range(1,10))
<generator object <genexpr> at 0x000001AD89A93350>
>>> #generator expression
>>> {i for i in range(1,10)}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> {i : i ** 2 for i in range(1,10)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> data {i : i ** 2 for i in range(1,10)}
SyntaxError: invalid syntax
>>> data = {i : i ** 2 for i in range(1,10)}
>>> data
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> data[1]
1
>>> data[2]
4
>>> data[3]
9
>>> data[5]
25
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2A/dict_exercise.py =
['John', 'Shawn', 'Tom', 'Jerry', 'Harry']
[67, 77, 87, 98, 65]
['soccer', 'tennis', 'soccer', 'volleyball', 'tennis']
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2A/dict_exercise.py =
names : ['John', 'Shawn', 'Tom', 'Jerry', 'Harry']
marks : [67, 77, 87, 98, 65]
hobby : ['soccer', 'tennis', 'soccer', 'volleyball', 'tennis']
>>> len(data)
3
>>> data["names"]
['John', 'Shawn', 'Tom', 'Jerry', 'Harry']
>>> len(data["names"])
5
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2A/dict_exercise.py =
names : ['John', 'Shawn', 'Tom', 'Jerry', 'Harry']
marks : [67, 77, 87, 98, 65]
hobby : ['soccer', 'tennis', 'soccer', 'volleyball', 'tennis']
Shawn 77 tennis
Tom 87 soccer
Jerry 98 volleyball
>>> data['marks']
[67, 77, 87, 98, 65]
>>> data['marks'][0]
67
>>> data['marks'][0] >= 70
False
>>> data['marks'][1] >= 70
True
>>> data['marks'][2] >= 70
True
>>> import pandas as pd
>>> pd.DataFrame(data)
   names  marks       hobby
0   John     67      soccer
1  Shawn     77      tennis
2    Tom     87      soccer
3  Jerry     98  volleyball
4  Harry     65      tennis
>>> import matplotlib.pyplot as plt
>>> plt.bar(data['names'], data])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> plt.bar(data['names'], data['marks'])
<BarContainer object of 5 artists>
>>> plt.show()
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2A/cricapi.py ====
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['pid', 'profile', 'imageURL', 'battingStyle', 'bowlingStyle', 'majorTeams', 'currentAge', 'born', 'fullName', 'name', 'country', 'playingRole', 'v', 'data', 'ttl', 'provider', 'creditsLeft'])
>>> data['profile']
"\n\nSachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ever known. His batting was based on the purest principles: perfect balance, economy of movement, precision in stroke-making, and that intangible quality given only to geniuses - anticipation. If he didn't have a signature stroke - the upright, back-foot punch comes close - it's because he was equally proficient at each of the full range of orthodox shots (and plenty of improvised ones as well) and can pull them out at will.  \n\n"
>>> data_1 = data['data']
>>> type(data_1)
<class 'dict'>
>>> data_1.keys()
dict_keys(['bowling', 'batting'])
>>> batting = data_1['batting']
>>> type(batting)
<class 'dict'>
>>> batting.keys()
dict_keys(['listA', 'firstClass', 'T20Is', 'ODIs', 'tests'])
>>> test = batting['tests']
>>> type(test)
<class 'dict'>
>>> test.keys()
dict_keys(['50', '100', 'St', 'Ct', '6s', '4s', 'SR', 'BF', 'Ave', 'HS', 'Runs', 'NO', 'Inns', 'Mat'])
>>> test
{'50': '68', '100': '51', 'St': '0', 'Ct': '115', '6s': '69', '4s': '', 'SR': '', 'BF': '', 'Ave': '53.78', 'HS': '248*', 'Runs': '15921', 'NO': '33', 'Inns': '329', 'Mat': '200'}
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2A/cricapi.py ====


Sachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ever known. His batting was based on the purest principles: perfect balance, economy of movement, precision in stroke-making, and that intangible quality given only to geniuses - anticipation. If he didn't have a signature stroke - the upright, back-foot punch comes close - it's because he was equally proficient at each of the full range of orthodox shots (and plenty of improvised ones as well) and can pull them out at will.  


50 : 96
100 : 49
St : 0
Ct : 140
6s : 195
4s : 2016
SR : 86.23
BF : 21367
Ave : 44.83
HS : 200*
Runs : 18426
NO : 41
Inns : 452
Mat : 463
****************************************
50 : 68
100 : 51
St : 0
Ct : 115
6s : 69
4s : 
SR : 
BF : 
Ave : 53.78
HS : 248*
Runs : 15921
NO : 33
Inns : 329
Mat : 200
>>> 