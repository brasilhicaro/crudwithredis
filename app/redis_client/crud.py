from .connection import Connection
from redis.exceptions import ResponseError


class Crud:
    
    __db_connection: None
    
    def __init__(self) -> None:
        db = Connection.__init___
        self.__db_connection= db
            
      
    def save_hash(self,key:str, data:dict):
        try:
            self.__db_connection.hset(name=key, mapping=data)
        except ResponseError as e:
            print(e)
            
    def get_hash(self, key:str):
        try: 
            return self.__db_connection.hgetall(name = key)
        except ResponseError as e:
            print(e)
    
    def delete_hash(self,key: str, keys: list):
        try:
            self.__db_connection.hdel(key, *keys)
        except ResponseError as e:
            print(e)
        