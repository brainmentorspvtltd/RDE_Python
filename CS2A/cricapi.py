import urllib.request as url
import json

path = "https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=35320"
response = url.urlopen(path)

data = json.load(response)
print(data['profile'])

data_1 = data['data']
batting = data_1['batting']
odi = batting['ODIs']

for key in odi:
    print(key,":",odi[key])

print("*" * 40)

test = batting['tests']

for key in test:
    print(key,":",test[key])
