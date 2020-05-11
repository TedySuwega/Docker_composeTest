import time

import redis
from flask import Flask
# from flask_restful import Resource, Api


app=Flask(__name__)
# api = Api(app)
cache =redis.Redis(host='redis',port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    # count = get_hit_count()
    # return 'Hello my new friend!. \n We meet {} times today.'.format(count)
    return 'Heloo my new friend from the other universe!'

if __name__ == "__main__":
    app.run()