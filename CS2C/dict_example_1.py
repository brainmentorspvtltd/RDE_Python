data = {
    "names" : ['Ram','Shyam','Mohan','Aman','Suman'],
    "marks" : [67,88,76,90,62],
    "hobby" : ['cricket', 'football', 'cricket', 'football', 'chess']
    }

'''
for i in range(len(data['names'])):
    if data['hobby'][i] == 'cricket':
        print(data['names'][i],
              data['hobby'][i])
'''
for i in range(len(data['names'])):
    if data['marks'][i] >= 70:
        print(data['names'][i],
              data['hobby'][i],
              data['marks'][i])







