data = [
    {'id':1,'name':'Apple Iphone 12','brand':'Apple','cat':'Mobile','price':78000},
    {'id':2,'name':'Apple Iphone 11','brand':'Apple','cat':'Mobile','price':58000},
    {'id':3,'name':'Apple Iphone X','brand':'Apple','cat':'Mobile','price':50000},
    {'id':4,'name':'Apple Iphone 12 pro','brand':'Apple','cat':'Mobile','price':138000},
    {'id':5,'name':'Mi Note 6','brand':'Xiaomi','cat':'Mobile','price':18000},
    {'id':6,'name':'Adidas Sports Shoes','brand':'Adidas','cat':'Shoes','price':3800},
    {'id':7,'name':'Leather Jacket','brand':'Zara','cat':'Clothes','price':8000},
    {'id':8,'name':'Samsung Galaxy Tab','brand':'Samsung','cat':'Tablet','price':18000},
    {'id':9,'name':'Samsung Tv','brand':'Samsung','cat':'TV','price':58000},
    ]

query = input("Enter your search : ")
query = query.lower()

'''
for i in range(len(data)):
    if query in data[i]['name'].lower() or query in data[i]['brand'].lower():
        print(data[i])
'''
for i in range(len(data)):
    condition_1 = query in data[i]['name'].lower()
    condition_2 = query in data[i]['brand'].lower()
    if  condition_1 or condition_2 :
        print(data[i])








