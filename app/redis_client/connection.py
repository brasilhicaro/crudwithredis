from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv

class connection:
    def connection_database()-> None : 
        try:
            __client_redis = Redis(
            host= 'REDIS_HOST',
            port= 'REDIS_PORT',
            password= 'REDIS_PASSWORD',
            )

            __client_redis.set('foo','bar')
            print('CONNECTED TO DATABASE')
        except ConnectionError as e:
            print(e)