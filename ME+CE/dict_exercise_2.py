data = {
    "names" : ['Ram','Shyam','Kunal','Aman'],
    "marks" : [67,77,87,59],
    "hobby" : ['cricket','football','chess','cricket']
    }

for i in range(len(data['names'])):
    if data['marks'][i] > 70:
        print(data['names'][i], data['marks'][i])
