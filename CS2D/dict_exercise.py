#data = [{},{},{}]

data = {'id' : [101,102,103,104,105],
        'names' : ['John','Shawn','Tom','Jerry','Peter'],
        'dept' : ['CS','EC','CS','CS','EC'],
        'marks' : [88, 91, 73, 60, 65]}

for i in range(len(data['id'])):
    #if data['marks'][i] >= 70:
    if data['dept'][i] == 'CS':
        print(data['names'][i], data['dept'][i], data['marks'][i])
