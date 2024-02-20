#Dillehay, Jennifer
#M06 15.1

import redis
conn=redis.Redis()
print("Every good movie deserves pie")
while True:
    msg = conn.blpop("movie")
    if not msg:
        break
    val = msg[1].decode("utf-8")
    if val == "quit":
        break
    print("Eating my after-dinner pie")
