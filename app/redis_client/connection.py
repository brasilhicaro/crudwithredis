from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv

class Connection:
    __client_redis : None
    
    def __init__(self):
        self.__client_redis  = Connection.connection_database(self)
    def connection_database(self)-> None : 
        try:
            self.__client_redis = Redis(
            host= 'REDIS_HOST',
            port= 'REDIS_PORT',
            password= 'REDIS_PASSWORD',
            )

            self.__client_redis.set('foo','bar')
            print('CONNECTED TO DATABASE')
        except ConnectionError as e:
            print(e)