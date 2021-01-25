names = ['John','Shawn','Tom','Jerry','Harry']
marks = [67,77,87,98,65]
hobby = ['soccer','tennis','soccer','volleyball','tennis']

data = {"names" : names, "marks" : marks, "hobby" : hobby}

for item in data:
    print(item ,":", data[item])

for i in range(len(data['names'])):
    if data['marks'][i] >= 70:
        print(data["names"][i],
              data["marks"][i],
              data["hobby"][i])
