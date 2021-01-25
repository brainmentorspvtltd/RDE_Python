import urllib.request as url
import json

name = input("Enter player name : ")
path = "https://cricapi.com/api/playerFinder?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&name={}".format(name)
response = url.urlopen(path)
data = json.load(response)
data_1 = data['data']
id = data_1[0]['pid']

path = 'https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid={}'.format(id)

response = url.urlopen(path)
data = json.load(response)

profile = data['profile']
data_1 = data['data']
batting = data_1['batting']
odi = batting['ODIs']

print(profile)
for item in odi:
    print(item,":",odi[item])

