# Task 1
import requests as rq
import pprint as pr

ht = {'q':'html'}

zap = rq.get('https://api.github.com', params=ht)
print(zap.status_code)
pr.pprint(zap.json())

# Task 2
import requests as rq
import pprint as pr

ht =('https://jsonplaceholder.typicode.com/posts')
ur = {'userId':1}

zap = rq.get(ht, params=ur)
print(zap.status_code)
pr.pprint(zap.json())


# Task 3

import requests as rq
import pprint as pr

ht =('https://jsonplaceholder.typicode.com/posts')
db =  {"title":"foo",
       "body":"bar",
       "userId":1
}

zap = rq.post(ht, data=db)
pr.pprint(zap.json())
