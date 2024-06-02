#!/usr/bin/python3
"""NEW Engine"""
from os import getenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import models

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
        """ """
        # from models.city import City
        # from models.review import Review
        # from models.state import State
        # from models.user import User
        # from models.amenity import Amenity
        # from models.place import Place
        dic = {}
        

        if cls is not None:
            queries = self.__session.query(cls)
            # print("Class exists")
            # print(queries)
            for instance in queries:
                # print("Inside the loop")
                key = instance.__class__.__name__ + '.' + instance.id
                dic[key] = instance

        else:
            for key, value in models.the_tables.items():
                queries = self.__session.query(value)
                for instance in queries:
                    key = instance.__class__.__name__ + '.' + instance.id
                    dic[key] = instance
        return dic

    def new(self, obj):
        """add the object to the current database session"""
        try:
            self.__session.add(obj)
        except Exception as e:
            print(f"Error saving changes: {e}")
            raise

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
            print("Changes saved successfully.")
        except Exception as e:
            print(f"Error saving changes: {e}")
            raise

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        try:
            Base.metadata.create_all(self.__engine)
            s1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(s1)
            self.__session = Session()
        except Exception as e:
            print(f"Error reloading database: {e}")
            raise

    def close(self):
        """ calls remove() """
        try:
            self.__session.close()
        except Exception as e:
            print(f"Error closing session: {e}")
            raise
