#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class that defines common attributes/methods."""

    def __init__(self, *args, **kwargs):
        from models import storage  # Import here to avoid circular dependency
        """ Initialize a new instance of BaseModel. """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                #Skip the __class__ attribute
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ Update 'updated_at' with the current datetime. """
        from models import storage  # Import here to avoid circular dependency
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance."""
        # Copy the __dict__ to avoid modifying the original instance attributes
        dictionary = self.__dict__.copy()
        # Add the class name to the dictionary
        dictionary['__class__'] = self.__class__.__name__
        # Convert datetime attributes to ISO format strings
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
