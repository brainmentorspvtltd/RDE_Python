Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [56,'Ram',78,'Delhi']
>>> data = {'id':56, 'name':'Ram', 'marks':78, 'address':'Delhi'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['id']
56
>>> data['name']
'Ram'
>>> data['marks']
78
>>> data['address']
'Delhi'
>>> data['address'] = 'UP'
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP'}
>>> data['hobby'] = 'Dance'
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance'}
>>> len(data)
5
>>> for i in range(len(data)):
	print(data[i])

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(data[i])
KeyError: 0
>>> for key in data:
	print(key)

	
id
name
marks
address
hobby
>>> for key in data:
	print(key, data[key])

	
id 56
name Ram
marks 78
address UP
hobby Dance
>>> {x : x for x in range(1,10)}
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>> {x : x**2 for x in range(1,10)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> data.keys()
dict_keys(['id', 'name', 'marks', 'address', 'hobby'])
>>> data.values()
dict_values([56, 'Ram', 78, 'UP', 'Dance'])
>>> data.items()
dict_items([('id', 56), ('name', 'Ram'), ('marks', 78), ('address', 'UP'), ('hobby', 'Dance')])
>>> data['year']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data['year']
KeyError: 'year'
>>> data.get('year')
>>> data.get('year', 'Not available')
'Not available'
>>> data.get('name', 'Not available')
'Ram'
>>> data.setdefault('year')
>>> dta
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dta
NameError: name 'dta' is not defined

>>> at
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    at
NameError: name 'at' is not defined
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance', 'year': None}
>>> data['year'] = 2
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance', 'year': 2}
>>> data.setdefault('sem', '3rd')
'3rd'
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance', 'year': 2, 'sem': '3rd'}
>>> data.pop('sem')
'3rd'
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance', 'year': 2}
>>> data.popitem()
('year', 2)
>>> data
{'id': 56, 'name': 'Ram', 'marks': 78, 'address': 'UP', 'hobby': 'Dance'}
>>> names = ['Ram','Shyam','Laxman','Gopal','Manoj']
>>> marks = [67,77,87,59,72]
>>> address = ['Delhi','Gzb','Delhi','Gzb','Gzb']
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/dict_exercise.py =
>>> data
{'names': ['Ram', 'Shyam', 'Laxman', 'Gopal', 'Manoj'], 'marks': [67, 77, 87, 59, 72], 'address': ['Delhi', 'Gzb', 'Delhi', 'Gzb', 'Gzb']}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/dict_exercise.py =
names : ['Ram', 'Shyam', 'Laxman', 'Gopal', 'Manoj']
marks : [67, 77, 87, 59, 72]
address : ['Delhi', 'Gzb', 'Delhi', 'Gzb', 'Gzb']
>>> data
{'names': ['Ram', 'Shyam', 'Laxman', 'Gopal', 'Manoj'], 'marks': [67, 77, 87, 59, 72], 'address': ['Delhi', 'Gzb', 'Delhi', 'Gzb', 'Gzb']}
>>> data['marks']
[67, 77, 87, 59, 72]
>>> data['marks'][0]
67
>>> data['marks'][0] > 70
False
>>> data['marks'][1] > 70
True
>>> data['marks'][2] > 70
True
>>> data['marks'][3] > 70
False
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/dict_exercise.py =
Shyam 77
Laxman 87
Manoj 72
>>> import pandas as pd
>>> pd.DataFrame(data)
    names  marks address
0     Ram     67   Delhi
1   Shyam     77     Gzb
2  Laxman     87   Delhi
3   Gopal     59     Gzb
4   Manoj     72     Gzb
>>> import matplotlib.pyplot as plt
>>> plt.bar(data['names'], data['marks'])
<BarContainer object of 5 artists>
>>> plt.show()
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['pid', 'country', 'profile', 'imageURL', 'battingStyle', 'bowlingStyle', 'majorTeams', 'currentAge', 'born', 'fullName', 'name', 'playingRole', 'v', 'data', 'ttl', 'provider', 'creditsLeft'])
>>> data['profile']
"\n\nBarring Sachin Tendulkar, MS Dhoni is arguably the most popular and definitely the most scrutinised cricketer from India. He has done so coming from the cricketing backwaters, the mining state of Jharkhand, and through a home-made batting and wicketkeeping technique, and a style of captaincy that scales the highs and lows of both conservatism and unorthodoxy. Under Dhoni's captaincy, India have won the top prize in all formats: the No.1 Test ranking for 18 months starting December 2009, the 50-over World Cup in 2011 and the World Twenty20 on his captaincy debut in 2007. \n\n"
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
>>> odi = batting['ODIs']
>>> type(odi\)
     
SyntaxError: unexpected character after line continuation character
>>> type(odi)
<class 'dict'>
>>> odi.keys()
dict_keys(['50', '100', 'St', 'Ct', '6s', '4s', 'SR', 'BF', 'Ave', 'HS', 'Runs', 'NO', 'Inns', 'Mat'])
>>> odi
{'50': '66', '100': '10', 'St': '103', 'Ct': '288', '6s': '213', '4s': '752', 'SR': '88.45', 'BF': '11080', 'Ave': '51.85', 'HS': '183*', 'Runs': '9801', 'NO': '76', 'Inns': '265', 'Mat': '308'}
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
50 : 66
100 : 10
St : 103
Ct : 288
6s : 213
4s : 752
SR : 88.45
BF : 11080
Ave : 51.85
HS : 183*
Runs : 9801
NO : 76
Inns : 265
Mat : 308
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====


Barring Sachin Tendulkar, MS Dhoni is arguably the most popular and definitely the most scrutinised cricketer from India. He has done so coming from the cricketing backwaters, the mining state of Jharkhand, and through a home-made batting and wicketkeeping technique, and a style of captaincy that scales the highs and lows of both conservatism and unorthodoxy. Under Dhoni's captaincy, India have won the top prize in all formats: the No.1 Test ranking for 18 months starting December 2009, the 50-over World Cup in 2011 and the World Twenty20 on his captaincy debut in 2007. 


50 : 66
100 : 10
St : 103
Ct : 288
6s : 213
4s : 752
SR : 88.45
BF : 11080
Ave : 51.85
HS : 183*
Runs : 9801
NO : 76
Inns : 265
Mat : 308
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
Enter player name : yuvraj
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['data', 'ttl', 'cache3', 'v', 'provider', 'creditsLeft'])
>>> data['data']
[{'pid': 36084, 'fullName': 'Yuvraj Singh', 'name': 'Yuvraj Singh'}, {'pid': 581607, 'fullName': 'Yuvraj Paul Dayal', 'name': 'Yuvraj Paul Dayal'}, {'pid': 969367, 'fullName': 'Yuvraj Chudasama', 'name': 'Yuvraj Chudasama'}, {'pid': 1057451, 'fullName': 'R Yuvraj', 'name': 'R Yuvraj'}, {'pid': 1072457, 'fullName': 'Yuvraj Singh', 'name': 'Yuvraj Singh'}, {'pid': 1090829, 'fullName': 'Yuvraj Odedra', 'name': 'Yuvraj Odedra'}, {'pid': 1175463, 'fullName': 'Yuvraj Chaudhary', 'name': 'Yuvraj Chaudhary'}]
>>> data_1 = data['data']
>>> type(data_1)
<class 'list'>
>>> data_1[0]
{'pid': 36084, 'fullName': 'Yuvraj Singh', 'name': 'Yuvraj Singh'}
>>> data_1[0]['pid']
36084
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
Enter player name : sehwag


Virender Sehwag has constructed an extraordinary career with a relentless quest, and a genius, for boundary hitting. With minimal footwork but maximum intent, he has piled Test runs at a faster pace than anyone in the history of cricket. Bowlers must always fancy their chances against a batsman who plays so many strokes; it's just that Sehwag fancies his chances against them much more. 


50 : 38
100 : 15
St : 0
Ct : 93
6s : 136
4s : 1132
SR : 104.33
BF : 7929
Ave : 35.05
HS : 219
Runs : 8273
NO : 9
Inns : 245
Mat : 251
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
Enter player name : virat
Traceback (most recent call last):
  File "C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py", line 19, in <module>
    odi = batting['ODIs']
KeyError: 'ODIs'
>>> 
==== RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2B/cricapi.py ====
Enter player name : kohli


India has given to the world many a great cricketer but perhaps none as ambitious as Virat Kohli. To meet his ambition, Kohli employed the technical assiduousness of Sachin Tendulkar and fitness that was in the league of top athletes in the world, not just cricketers. As a result, Kohli became the most consistent all-format accumulator of his time, making jaw-dropping chases look easy, and finding, in his own words, the safest possible way to score runs. Plenty of them. 


50 : 58
100 : 43
St : 0
Ct : 128
6s : 121
4s : 1116
SR : 93.25
BF : 12726
Ave : 59.33
HS : 183
Runs : 11867
NO : 39
Inns : 239
Mat : 248
>>> 