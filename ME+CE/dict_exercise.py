data = [
    {'name': 'Gopal', 'sal': 45000, 'dept': 'IT'},
    {'name': 'Kunal', 'sal': 42000, 'dept': 'HR'},
    {'name': 'Aman', 'sal': 35000, 'dept': 'HR'}
    ]

for i in range(len(data)):
    '''
    if data[i]['sal'] > 40000:
        print(data[i])
    '''
    if data[i]['dept'] == 'HR':
        print(data[i])

