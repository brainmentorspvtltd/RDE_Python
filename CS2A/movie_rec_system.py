movies = {
    "action" : ['avengers','thor','hulk','baahubali','kgf',
                'MI', 'ironman', 'batman', 'superman', 'spiderman'],
    "comedy" : ['dhamaal', 'golmaal', 'dhol', 'hera pheri',
                'the mask','laxmi','stree'],
    "horror" : ['nun', 'laxmi','stree','ring','oculus'],
    "thriller" : ['kgf','MI','departed','inception']
    }
user = {'ironman', 'thor', 'laxmi', 'golmaal', 'hulk', 'kgf'}

scores = {}
for key in movies:
    m = movies[key]
    numer = len(user.intersection(m))
    denom = len(user.union(m))
    score = numer/denom
    scores[key] = round(score,2)

print(scores)

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

rec_movies = set(movies[category]) - user
print("You should watch :",rec_movies)













