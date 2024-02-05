#!/usr/bin/python3
"""contains the entry point 
of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class definition """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

