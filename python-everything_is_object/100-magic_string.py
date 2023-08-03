#!/usr/bin/python3
def magic_string():
<<<<<<< HEAD
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string.n - 1) + "Holberton")
=======
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ', '.join(['Holberton']*magic_string.counter)
>>>>>>> 57b2f5aa754b5d779c79e9cf7f491fe58932a3ab
