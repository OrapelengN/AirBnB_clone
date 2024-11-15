#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
