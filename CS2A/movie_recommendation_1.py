movies = {
    "action" : ['avengers','thor','hulk','baahubali','kgf',
                'MI', 'ironman', 'batman', 'superman', 'spiderman'],
    "comedy" : ['dhamaal', 'golmaal', 'dhol', 'hera pheri',
                'the mask','laxmi','stree'],
    "horror" : ['nun', 'laxmi','stree','ring','oculus'],
    "thriller" : ['kgf','MI','departed','inception']
    }

user = {'ironman', 'thor', 'laxmi', 'golmaal', 'hulk', 'dhol'}

scores = {}
for key in movies:
    x = movies[key]
    numer = set(x).intersection(user)
    denom = set(x).union(user)
    score = len(numer) / len(denom)
    scores[key] = round(score,2)

print(scores)
#max(scores.items(), key = lambda x : x[1])

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

print("User watched {} movies max".format(category))

recommended_movies = set(movies[category]) - user
print("Movies recommended : ",recommended_movies)







