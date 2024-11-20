#!/usr/bin/python3
"""Entry point for the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel


# Dictionary to store valid classes
CLASSES = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline for clean output
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in CLASSES:
            print("** class doesn't exist **")
            return
        instance = CLASSES[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

        #Test after running destroy
        print(storage.all())

    def save(self):
        """Serializes objects to the JSON file."""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file back into objects."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for k, v in data.items():
                    cls_name = v["__class__"]
                    self.__objects[k] = CLASSES[cls_name](**v)
        except FileNotFoundError:
            pass

    def do_all(self, arg):
        """ Show all instances of a class,
            or all classes if no class is specified."""
        if arg and arg not in CLASSES:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        if arg:
            objs = {k: v for k, v in objs.items() if k.startswith(arg + ".")}
        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Update an instance's attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"') # Handle string values

        # Handle type casting for known attributes
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                pass # Leave as string if type casting fails
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
