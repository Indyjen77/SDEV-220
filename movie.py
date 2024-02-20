#Dillehay, Jennifer
#M06 15.1

import redis
conn = redis.Redis()
print("The movie marathon is starting")
movies = ["True Romance" , "Pan's Labryinth" , "Mad Max" , "Harry Potter and the Chamber of Secrets"]
for movie in movies:
    msg = movie.encode("utf-8")
    conn.rpush("movies",msg)
    print("Movie" , movie)
conn.rpush("movies" , "Quit")
print("Movies are done")
