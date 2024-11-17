#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class that defines common attributes/methods."""

    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of BaseModel. """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs and isinstance(self.created_at, str):
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs and isinstance(self.updated_at, str):
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """ Update 'updated_at' with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance. """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """ Return a string representation of the instance. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
