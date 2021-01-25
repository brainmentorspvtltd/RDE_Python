names = ['Ram','Shyam','Laxman','Gopal','Manoj']
marks = [67,77,87,59,72]
address = ['Delhi','Gzb','Delhi','Gzb','Gzb']

data = {'names' : names, 'marks' : marks, 'address' : address}
'''
for item in data:
    print(item, ":", data[item])
'''
for i in range(len(data['names'])):
    if data['marks'][i] >= 70:
        print(data['names'][i], data['marks'][i])
