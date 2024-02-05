#!/usr/bin/python3
""" class BaseModel that defines all common
attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ class basemodel"""

    def __init__(self):
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)
