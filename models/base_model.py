#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base model that defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def save(self):
        """Updates the updated_at attribute with current datetime."""
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
