data = [
    {'name':'Ram','dept':'IT','sal':45000,'desig':'Developer'},
    {'name':'Shyam','dept':'HR','sal':48000,'desig':'Manager'},
    {'name':'Mohan','dept':'IT','sal':35000,'desig':'Developer'},
    {'name':'Pooja','dept':'Sales','sal':49000,'desig':'Manager'},
    {'name':'Geeta','dept':'IT','sal':50000,'desig':'Tester'},
    ]
'''
for i in range(len(data)):
    if data[i]['dept'] == 'IT':
        print(data[i])
'''
dept = input("Enter emp dept : ")
dept = dept.lower()
for i in range(len(data)):
    if data[i]['dept'].lower() == dept:
        print(data[i])









