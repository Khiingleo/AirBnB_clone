#!/usr/bin/python3
""" Defines a HBNBCommand class"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    """ parses the input of the user"""
    return tuple(arg.split())


class HBNBCommand(cmd.Cmd):
    """ command interpreter for the HBNB """
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ exits the program """
        print()
        return True

    def emptyline(self):
        """ Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, sabe it and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exits **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_key = "{}.{}".format(class_name, args[1])
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_key = "{}.{}".format(class_name, args[1])
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of all instances"""
        instances = storage.all()
        if not arg:
            print([str(instance) for instance in instances.values()])
            return

        class_name = arg
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        filtered = [str(instance) for key, instance in instances.items() if
                    key.split('.')[0] == class_name]
        print(filtered)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = parse(arg)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
