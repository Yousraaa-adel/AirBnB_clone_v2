#!/usr/bin/python3
"""NEW Engine"""
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

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

        
    def all(self, cls=None):
        dic={}
        # if type(cls) is str:
        #     cls = eval(cls)
        if cls is not None:
            queries = self.__session.query(cls)
            print("Class exists")
            print(queries)
            for instance in queries:
                print("Inside the loop")
                key = instance.__class__.__name__ + '.' + instance.id
                dic[key] = instance

        else:
            classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
            # if type(cls) is str:
            #     cls = eval(cls)
            
            for key, value in classes.items():
                queries = self.__session.query(value)
                for instance in queries:
                    key = instance.__class__.__name__ + '.' + instance.id
                    dic[key] = instance
        return dic
                  
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
            
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        # print(self.__session)
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            
    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        s1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session= scoped_session(s1)
        self.__session = Session()
