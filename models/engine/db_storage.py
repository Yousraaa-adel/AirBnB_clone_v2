#!/usr/bin/python3
"""NEW Engine"""
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String
from models.base_model import Base

class DBStorage():
    """DBStorage class"""
    
    __engine = None
    __session = None
    def __init__(self):
        """Constructor of DBStorage"""
        
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        
