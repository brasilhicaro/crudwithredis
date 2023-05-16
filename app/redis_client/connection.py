from redis import Redis
from redis.exceptions import ConnectionError

try:
    redis_client = Redis(host='localhost', port=6379, db=0)
except ConnectionError as e:
    print(e)
