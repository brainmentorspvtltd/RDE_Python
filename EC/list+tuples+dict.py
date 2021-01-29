Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [1,2,3,46,65,2,5,7,10.56,'hi']
>>> type(data)
<class 'list'>
>>> data[0]
1
>>> data[0:5]
[1, 2, 3, 46, 65]
>>> data[::-1]
['hi', 10.56, 7, 5, 2, 65, 46, 3, 2, 1]
>>> data = []
>>> data.append(10)
>>> data
[10]
>>> data.append(20)
>>> data
[10, 20]
>>> data.append(50)
>>> data
[10, 20, 50]
>>> #LIFO - Last In First Out
>>> data.append(2,3,5,6,5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data.append(2,3,5,6,5)
TypeError: list.append() takes exactly one argument (5 given)
>>> data.append([2,3,5,6,5])
>>> data
[10, 20, 50, [2, 3, 5, 6, 5]]
>>> data.pop()
[2, 3, 5, 6, 5]
>>> data
[10, 20, 50]
>>> data.extend([2,3,4,5,7,4])
>>> data
[10, 20, 50, 2, 3, 4, 5, 7, 4]
>>> data + [67,5,6,7,5]
[10, 20, 50, 2, 3, 4, 5, 7, 4, 67, 5, 6, 7, 5]
>>> data * 2
[10, 20, 50, 2, 3, 4, 5, 7, 4, 10, 20, 50, 2, 3, 4, 5, 7, 4]
>>> data - 2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data - 2
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> data.insert(5,100)
>>> data
[10, 20, 50, 2, 3, 100, 4, 5, 7, 4]
>>> data.pop(-2)
7
>>> data.pop(3)
2
>>> data.remove(0)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.remove(0)
ValueError: list.remove(x): x not in list
>>> data.remove(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
>>> data
[10, 20, 50, 3, 100, 4, 5, 4]
>>> data.remove(4)
>>> data
[10, 20, 50, 3, 100, 5, 4]
>>> data[0] = 11
>>> data
[11, 20, 50, 3, 100, 5, 4]
>>> sorted(data)
[3, 4, 5, 11, 20, 50, 100]
>>> sorted(data, reverse=True)
[100, 50, 20, 11, 5, 4, 3]
>>> data
[11, 20, 50, 3, 100, 5, 4]
>>> data.sort()
>>> data
[3, 4, 5, 11, 20, 50, 100]
>>> 
>>> 
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = 10,20,11,3
>>> type(x)
<class 'tuple'>
>>> x = (10,20,11,3)
>>> type(x)
<class 'tuple'>
>>> x[0] = 5
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x[0] = 5
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = 'Ram', 56, 60000, 'IT'
>>> #unpacking
>>> name, age, sal, dept = data
>>> name
'Ram'
>>> age
56
>>> sal
60000
>>> dept
'IT'
>>> name, age, sal = data
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    name, age, sal = data
ValueError: too many values to unpack (expected 3)
>>> name, age, *sal = data
>>> name
'Ram'
>>> age
56
>>> sal
[60000, 'IT']
>>> data = {}
>>> type(data)
<class 'dict'>
>>> data = dict()
>>> data = {'name' : 'Ram', 'age' : 50, 'sal' : 56000}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ram'
>>> data['age']
50
>>> data['dept']
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    data['dept']
KeyError: 'dept'
>>> data['dept'] = 'IT'
>>> data
{'name': 'Ram', 'age': 50, 'sal': 56000, 'dept': 'IT'}
>>> data['name'] = 'Shyam'
>>> data
{'name': 'Shyam', 'age': 50, 'sal': 56000, 'dept': 'IT'}
>>> 
=== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/codiv-19-api.py ==
>>> response
<http.client.HTTPResponse object at 0x000001F58B8A81F0>
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> states[-1]
{'an': '0', 'ap': '0', 'ar': '0', 'as': '0', 'br': '2', 'ch': '0', 'ct': '35', 'date': '28-Jan-21', 'dateymd': '2021-01-28', 'dd': '0', 'dl': '6', 'dn': '0', 'ga': '2', 'gj': '2', 'hp': '0', 'hr': '0', 'jh': '3', 'jk': '1', 'ka': '2', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '50', 'ml': '0', 'mn': '0', 'mp': '3', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '9', 'py': '1', 'rj': '2', 'sk': '0', 'status': 'Deceased', 'tg': '1', 'tn': '6', 'tr': '0', 'tt': '162', 'un': '0', 'up': '6', 'ut': '3', 'wb': '9'}
>>> len(states)
963
>>> 963 / 3
321.0
>>> 
=== RESTART: C:/Users/acer/OneDrive/PythonRDE/EC/codiv-19-api.py ==
>>> len(confirmed)
321
>>> confirmed[100]
{'an': '0', 'ap': '443', 'ar': '9', 'as': '267', 'br': '228', 'ch': '5', 'ct': '47', 'date': '22-Jun-20', 'dateymd': '2020-06-22', 'dd': '0', 'dl': '2909', 'dn': '15', 'ga': '46', 'gj': '563', 'hp': '54', 'hr': '390', 'jh': '42', 'jk': '132', 'ka': '249', 'kl': '138', 'la': '10', 'ld': '0', 'mh': '3721', 'ml': '2', 'mn': '57', 'mp': '175', 'mz': '1', 'nl': '69', 'or': '143', 'pb': '161', 'py': '17', 'rj': '302', 'sk': '0', 'status': 'Confirmed', 'tg': '872', 'tn': '2710', 'tr': '16', 'tt': '13560', 'un': '-1295', 'up': '591', 'ut': '58', 'wb': '413'}
>>> confirmed[100]['up']
'591'
>>> confirmed[200]['up']
'4226'
>>> confirmed[200]['date']
'30-Sept-20'
>>> confirmed[300]['date'], confirmed[300]['up']
('08-Jan-21', '767')
>>> 