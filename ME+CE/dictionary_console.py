Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> for i in range(1,51):
	x.append(i)

	
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> x = []
>>> for i in range(1,51):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> x = [for i in range(1,11)]
SyntaxError: invalid syntax
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [i for i in range(1,11) if i % 2 == 0]
>>> x
[2, 4, 6, 8, 10]
>>> x = [i,j for i in range(1,11) for j in range(1,5)]
SyntaxError: invalid syntax
>>> x = [[i,j] for i in range(1,11) for j in range(1,5)]
>>> x
[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4], [6, 1], [6, 2], [6, 3], [6, 4], [7, 1], [7, 2], [7, 3], [7, 4], [8, 1], [8, 2], [8, 3], [8, 4], [9, 1], [9, 2], [9, 3], [9, 4], [10, 1], [10, 2], [10, 3], [10, 4]]
>>> x = [[i,j] for i in range(1,11) for j in range(1,5) if i == j]
>>> x
[[1, 1], [2, 2], [3, 3], [4, 4]]
>>> x = [[i,j] for i in range(1,11) for j in range(1,5) if i != j]
>>> x
[[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4], [6, 1], [6, 2], [6, 3], [6, 4], [7, 1], [7, 2], [7, 3], [7, 4], [8, 1], [8, 2], [8, 3], [8, 4], [9, 1], [9, 2], [9, 3], [9, 4], [10, 1], [10, 2], [10, 3], [10, 4]]
>>> 
>>> 
>>> 
>>> 
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = ()
>>> x = 10,11,14,22,5,6,7,3
>>> x = (10,11,14,22,5,6,7,3)
>>> x
(10, 11, 14, 22, 5, 6, 7, 3)
>>> x.count(5)
1
>>> x.index(11)
1
>>> x[0]
10
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x = (12,2,4,5,6.5,'hi')
>>> x[0:4]
(12, 2, 4, 5)
>>> data = 'Ram', 20, 'RDEC', 4
>>> type(data)
<class 'tuple'>
>>> name, age, college, year = data
>>> name
'Ram'
>>> age
20
>>> college
'RDEC'
>>> year
4
>>> name, age, college = data
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    name, age, college = data
ValueError: too many values to unpack (expected 3)
>>> name, age, *college = data
>>> name
'Ram'
>>> age
20
>>> college
['RDEC', 4]
>>> 
>>> 
>>> 
>>> 
>>> data = ['Ram',67,'IT','Cricket',45000]
>>> data = {'name' : 'Ram', 'id' : 101, 'dept' : 'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ram'
>>> data['id']
101
>>> data['id']
101
>>> data['dept']
'IT'
>>> data['sal'] = 45000
>>> data
{'name': 'Ram', 'id': 101, 'dept': 'IT', 'sal': 45000}
>>> data['name'] = 'Shyam'
>>> data
{'name': 'Shyam', 'id': 101, 'dept': 'IT', 'sal': 45000}
>>> for item in data:
	print(item)

	
name
id
dept
sal
>>> for item in data:
	print(item, data[item])

	
name Shyam
id 101
dept IT
sal 45000
>>> for item in data:
	print(item,"=", data[item])

	
name = Shyam
id = 101
dept = IT
sal = 45000
>>> data['name'] = 'Gopal'
>>> data
{'name': 'Gopal', 'id': 101, 'dept': 'IT', 'sal': 45000}
>>> data['sal'] = data['sal'] + 5000
>>> data
{'name': 'Gopal', 'id': 101, 'dept': 'IT', 'sal': 50000}
>>> data.keys()
dict_keys(['name', 'id', 'dept', 'sal'])
>>> data.values()
dict_values(['Gopal', 101, 'IT', 50000])
>>> data.items()
dict_items([('name', 'Gopal'), ('id', 101), ('dept', 'IT'), ('sal', 50000)])
>>> data['designation']
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    data['designation']
KeyError: 'designation'
>>> data.get('designation')
>>> data.get('designation', 'Not available')
'Not available'
>>> data.get('name', 'Not available')
'Gopal'
>>> data.get('xyz', 'Not available')
'Not available'
>>> data.pop()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.pop('sal')
50000
>>> data
{'name': 'Gopal', 'id': 101, 'dept': 'IT'}
>>> data.popitem()
('dept', 'IT')
>>> data.popitem()
('id', 101)

>>> data
{'name': 'Gopal'}
>>> data.setdefault('sal')
>>> data
{'name': 'Gopal', 'sal': None}
>>> data['sal'] = 45000
>>> data.setdefault('dept', 'IT')
'IT'
>>> data
{'name': 'Gopal', 'sal': 45000, 'dept': 'IT'}
>>> data_1 = {'address' : 'Delhi', 'ph' : 809009099}
>>> data.update(data_1)
>>> data
{'name': 'Gopal', 'sal': 45000, 'dept': 'IT', 'address': 'Delhi', 'ph': 809009099}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/dict_exercise.py
{'name': 'Gopal', 'sal': 45000, 'dept': 'IT'}
{'name': 'Kunal', 'sal': 42000, 'dept': 'HR'}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/dict_exercise.py
{'name': 'Kunal', 'sal': 42000, 'dept': 'HR'}
{'name': 'Aman', 'sal': 35000, 'dept': 'HR'}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/dict_exercise.py
{'name': 'Kunal', 'sal': 42000, 'dept': 'HR'}
{'name': 'Aman', 'sal': 35000, 'dept': 'HR'}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/dict_exercise_2.py
Shyam 77
Kunal 87
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/covid-19_api.py =
>>> response
<http.client.HTTPResponse object at 0x0000028F8B5ECBE0>
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/covid-19_api.py =
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> states[0]['up']
'12'
>>> states[0]['dl']
'7'
>>> states[200]
{'an': '0', 'ap': '2', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '19-May-20', 'dateymd': '2020-05-19', 'dd': '0', 'dl': '6', 'dn': '0', 'ga': '0', 'gj': '25', 'hp': '1', 'hr': '0', 'jh': '0', 'jk': '2', 'ka': '3', 'kl': '0', 'la': '0', 'ld': '0', 'mh': '76', 'ml': '0', 'mn': '0', 'mp': '6', 'mz': '0', 'nl': '0', 'or': '1', 'pb': '1', 'py': '0', 'rj': '5', 'sk': '0', 'status': 'Deceased', 'tg': '4', 'tn': '3', 'tr': '0', 'tt': '146', 'un': '0', 'up': '5', 'ut': '0', 'wb': '6'}
>>> len(data)
1
>>> len(states)
963
>>> len(states) / 3
321.0
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/covid-19_api.py =
>>> len(recovered)
321
>>> len(confirmed)
321
>>> len(deceased)
321
>>> confirmed[-1]
{'an': '0', 'ap': '117', 'ar': '3', 'as': '29', 'br': '134', 'ch': '36', 'ct': '6451', 'date': '28-Jan-21', 'dateymd': '2021-01-28', 'dd': '0', 'dl': '199', 'dn': '0', 'ga': '85', 'gj': '346', 'hp': '60', 'hr': '97', 'jh': '62', 'jk': '63', 'ka': '550', 'kl': '5771', 'la': '17', 'ld': '0', 'mh': '2889', 'ml': '8', 'mn': '15', 'mp': '226', 'mz': '3', 'nl': '1', 'or': '113', 'pb': '200', 'py': '39', 'rj': '85', 'sk': '5', 'status': 'Confirmed', 'tg': '184', 'tn': '503', 'tr': '0', 'tt': '18910', 'un': '0', 'up': '248', 'ut': '82', 'wb': '289'}
>>> recovered[-1]
{'an': '2', 'ap': '128', 'ar': '3', 'as': '95', 'br': '281', 'ch': '24', 'ct': '6479', 'date': '28-Jan-21', 'dateymd': '2021-01-28', 'dd': '0', 'dl': '119', 'dn': '0', 'ga': '52', 'gj': '602', 'hp': '52', 'hr': '111', 'jh': '112', 'jk': '149', 'ka': '644', 'kl': '5594', 'la': '2', 'ld': '0', 'mh': '3181', 'ml': '7', 'mn': '23', 'mp': '321', 'mz': '7', 'nl': '5', 'or': '132', 'pb': '192', 'py': '29', 'rj': '188', 'sk': '3', 'status': 'Recovered', 'tg': '306', 'tn': '544', 'tr': '3', 'tt': '20315', 'un': '0', 'up': '380', 'ut': '178', 'wb': '367'}
>>> 
=== RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/cric_api.py ===
Traceback (most recent call last):
  File "C:/Users/acer/OneDrive/PythonRDE/ME+CE/cric_api.py", line 6, in <module>
    response = url.urlopen()
TypeError: urlopen() missing 1 required positional argument: 'url'
>>> 
=== RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/cric_api.py ===
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['pid', 'country', 'profile', 'imageURL', 'battingStyle', 'bowlingStyle', 'majorTeams', 'currentAge', 'born', 'fullName', 'name', 'playingRole', 'v', 'data', 'ttl', 'provider', 'creditsLeft'])
>>> data['profile']
"\n\nVirender Sehwag has constructed an extraordinary career with a relentless quest, and a genius, for boundary hitting. With minimal footwork but maximum intent, he has piled Test runs at a faster pace than anyone in the history of cricket. Bowlers must always fancy their chances against a batsman who plays so many strokes; it's just that Sehwag fancies his chances against them much more. \n\n"
>>> data_1 = data['data']
>>> type(data_1)
<class 'dict'>
>>> data_1.keys()
dict_keys(['bowling', 'batting'])
>>> bat = data_1['batting']
>>> type(bat)
<class 'dict'>
>>> bat.keys()
dict_keys(['listA', 'firstClass', 'T20Is', 'ODIs', 'tests'])
>>> odi = bat['ODIs']
>>> type(odi)
<class 'dict'>
>>> odi.keys()
dict_keys(['50', '100', 'St', 'Ct', '6s', '4s', 'SR', 'BF', 'Ave', 'HS', 'Runs', 'NO', 'Inns', 'Mat'])
>>> print(odi)
{'50': '38', '100': '15', 'St': '0', 'Ct': '93', '6s': '136', '4s': '1132', 'SR': '104.33', 'BF': '7929', 'Ave': '35.05', 'HS': '219', 'Runs': '8273', 'NO': '9', 'Inns': '245', 'Mat': '251'}
>>> 
=== RESTART: C:/Users/acer/OneDrive/PythonRDE/ME+CE/cric_api.py ===
{'50': '66', '100': '10', 'St': '103', 'Ct': '288', '6s': '213', '4s': '752', 'SR': '88.45', 'BF': '11080', 'Ave': '51.85', 'HS': '183*', 'Runs': '9801', 'NO': '76', 'Inns': '265', 'Mat': '308'}
>>> 