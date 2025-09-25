
import requests as rq
import pprint as pr

ht =('https://jsonplaceholder.typicode.com/posts')
db =  {"title":"foo",
       "body":"bar",
       "userId":1
}

zap = rq.post(ht, data=db)
pr.pprint(zap.json())

