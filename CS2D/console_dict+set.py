Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\acer\OneDrive\PythonRDE\CS2D\dict_exercise_2.py
Enter your search : apple
{'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}
{'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}
{'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}
{'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}

Sort results based on Price :
1. Low to High
2. High to Low

Enter your choice : 1
>>> data = [[1,'Akash',67],[7,'Bhanuj',87],[3,'Akshay',56]]
>>> sorted(data)
[[1, 'Akash', 67], [3, 'Akshay', 56], [7, 'Bhanuj', 87]]
>>> sorted(data, key = 1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sorted(data, key = 1)
TypeError: 'int' object is not callable
>>> sorted(data, key = str)
[[1, 'Akash', 67], [3, 'Akshay', 56], [7, 'Bhanuj', 87]]
>>> sorted(data, key = int)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sorted(data, key = int)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> sorted(data, key = str)
[[1, 'Akash', 67], [3, 'Akshay', 56], [7, 'Bhanuj', 87]]
>>> def sort_data(x):
	return x[1]

>>> sorted(data, key = sort_data)
[[1, 'Akash', 67], [3, 'Akshay', 56], [7, 'Bhanuj', 87]]
>>> def sort_data(x):
	return x[2]

>>> sorted(data, key = sort_data)
[[3, 'Akshay', 56], [1, 'Akash', 67], [7, 'Bhanuj', 87]]
>>> data
[[1, 'Akash', 67], [7, 'Bhanuj', 87], [3, 'Akshay', 56]]
>>> sort_data(data[0])
67
>>> data[1]
[7, 'Bhanuj', 87]
>>> sort_data(data[1])
87
>>> sort_data(data[2])
56
>>> for i in range(len(data)):
	print(sort_data(data[i]))

	
67
87
56
>>> sorted(data, key = sort_data)
[[3, 'Akshay', 56], [1, 'Akash', 67], [7, 'Bhanuj', 87]]
>>> search_results
[{'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}, {'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}, {'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}, {'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}]
>>> sorted(data)
[[1, 'Akash', 67], [3, 'Akshay', 56], [7, 'Bhanuj', 87]]
>>> sorted(search_results)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sorted(search_results)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> def sort_data(dictionary):
	return dictionary['price']

>>> for i in range(len(search_results)):
	print(sort_data(search_results[i]))

	
78000
58000
50000
138000
>>> sorted(search_results, key = sort_data)
[{'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}, {'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}, {'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}, {'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}]
>>> sorted(search_results, key = lambda x : x['price'])
[{'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}, {'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}, {'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}, {'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}]
>>> 
= RESTART: C:\Users\acer\OneDrive\PythonRDE\CS2D\dict_exercise_2.py
Enter your search : apple
{'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}
{'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}
{'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}
{'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}

Sort results based on Price :
1. Low to High
2. High to Low

Enter your choice : 2
{'id': 4, 'name': 'Apple Iphone 12 pro', 'brand': 'Apple', 'cat': 'Mobile', 'price': 138000}
{'id': 1, 'name': 'Apple Iphone 12', 'brand': 'Apple', 'cat': 'Mobile', 'price': 78000}
{'id': 2, 'name': 'Apple Iphone 11', 'brand': 'Apple', 'cat': 'Mobile', 'price': 58000}
{'id': 3, 'name': 'Apple Iphone X', 'brand': 'Apple', 'cat': 'Mobile', 'price': 50000}
>>> x = {3,4,5,2,3,5,6,7,7,1,,}
SyntaxError: invalid syntax
>>> x = {3,4,5,2,3,5,6,7,7,1,23,11,456,53,5,8,4,3,3}
>>> x
{1, 2, 3, 4, 5, 6, 7, 456, 8, 11, 53, 23}
>>> y = {1,3,45,6,8,9,5,3,3,6,8,12,34,56,78,0}
>>> y
{0, 1, 34, 3, 5, 6, 8, 9, 12, 45, 78, 56}
>>> x & y
{1, 3, 5, 6, 8}
>>> x.intersection(y)
{1, 3, 5, 6, 8}
>>> x | y
{0, 1, 2, 3, 4, 5, 6, 7, 456, 8, 9, 11, 12, 78, 23, 34, 45, 53, 56}
>>> x.union(y)
{0, 1, 2, 3, 4, 5, 6, 7, 456, 8, 9, 11, 12, 78, 23, 34, 45, 53, 56}
>>> x - y
{2, 4, 7, 456, 11, 53, 23}
>>> y - x
{0, 34, 9, 12, 45, 78, 56}
>>> x.difference(y)
{2, 4, 7, 456, 11, 53, 23}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.3333333333333333, 'comedy': 0.18181818181818182, 'horror': 0.1, 'thriller': 0.1111111111111111}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
>>> scores
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
>>> max(scores)
'thriller'
>>> data = {'Ram':88,'Shyam':56,'Gopal':82}
>>> max(data)
'Shyam'
>>> scores.items()
dict_items([('action', 0.33), ('comedy', 0.18), ('horror', 0.1), ('thriller', 0.11)])
>>> max(scores.items())
('thriller', 0.11)
>>> max(scores.items(), key = lambda x : x[1])
('action', 0.33)
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
Traceback (most recent call last):
  File "C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py", line 25, in <module>
    if scores[key] == max_values:
NameError: name 'max_values' is not defined
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
User watched action movies max
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
User watched action movies max
Traceback (most recent call last):
  File "C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py", line 31, in <module>
    recommended_movies = movies[category] - user
TypeError: unsupported operand type(s) for -: 'list' and 'set'
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.33, 'comedy': 0.18, 'horror': 0.1, 'thriller': 0.11}
User watched action movies max
Movies recommended :  {'MI', 'avengers', 'spiderman', 'superman', 'baahubali', 'batman'}
>>> 
= RESTART: C:/Users/acer/OneDrive/PythonRDE/CS2D/movie_recommendation_1.py
{'action': 0.23, 'comedy': 0.3, 'horror': 0.1, 'thriller': 0.0}
User watched comedy movies max
Movies recommended :  {'the mask', 'dhamaal', 'stree', 'hera pheri'}
>>> 