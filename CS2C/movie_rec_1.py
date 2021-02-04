movies = {
    "action" : ['avengers','thor','hulk','baahubali','kgf',
                'MI', 'ironman', 'batman', 'superman', 'spiderman'],
    "comedy" : ['dhamaal', 'golmaal', 'dhol', 'hera pheri',
                'the mask','laxmi','stree'],
    "horror" : ['nun', 'laxmi','stree','ring','oculus'],
    "thriller" : ['kgf','MI','departed','inception']
    }
user = {'thor','hulk','laxmi','kgf','nun','dhol','stree','dhamaal'}

scores = {}
for key in movies:
    data = movies[key]
    data = set(data)
    numer = data.intersection(user)
    denom = data.union(user)
    score = len(numer) / len(denom)
    scores[key] = round(score,2)

print(scores)

max_value = max(scores.values())

for key in scores:
    if scores[key] == max_value:
        category = key
        break

data = movies[category]
rec_movies = set(data) - user
print("Recommended Movies",rec_movies)










