#!/usr/bin/python3
"""contains the entry point
of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition """
    prompt = '(hbnb) '
    classes = {
                "BaseModel": BaseModel, "User": User,
                "Place": Place, "State": State,
                "City": City, "Amenity": Amenity,
                "Review": Review
              }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        nameofclass = arg.split()[0]
        if nameofclass not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            nv_instance = HBNBCommand.classes[nameofclass]()
            nv_instance.save()
            print(nv_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        verif = arg.split()
        if len(verif) == 0:
            print("** class name missing **")
        elif len(verif) == 1:
            print("** instance id missing **")
        elif verif[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(verif[0], verif[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[str(verif[0])+"."+str(verif[1])])

    def do_destroy(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        verif = arg.split()
        if len(verif) == 0:
            print("** class name missing **")
        elif len(verif) == 1:
            print("** instance id missing **")
        elif verif[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(verif[0], verif[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[str(verif[0])+"."+str(verif[1])]

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        return_list = []
        if not arg:
            for key, value in storage.all().items():
                return_list.append(str(value))
        else:
            nameofclass = arg.split()[0]
            if nameofclass not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if nameofclass in key:
                    return_list.append(str(value))
        print(return_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file)."""
        verif = arg.split()
        if len(verif) == 0:
            print("** class name missing **")
            return
        nameofclass = verif[0]
        if nameofclass not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(verif) == 1:
            print("** instance id missing **")
            return
        instance_id = verif[1]
        val = str(nameofclass)+"."+str(instance_id)
        if val not in storage.all():
            print("** no instance found **")
            return
        if len(verif) == 2:
            print("** attribute name missing **")
            return
        nameofattr = verif[2]
        if len(verif) == 3:
            print("** value missing **")
            return
        valofattr = verif[3]
        instance = storage.all()[val]
        setattr(instance, nameofattr, valofattr)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
