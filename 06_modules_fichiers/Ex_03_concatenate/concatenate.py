#concatenate.py
import sys
import os

args = sys.argv[:]

if len(args) < 3:
    raise IndexError("Minimum 3 arguments")

if os.path.isfile(args[-1]):
    raise FileExistsError("Le fichier de destination existe déjà")
sys.exit(1)
for arg in args[1:-1]:
    if not os.path.isfile(arg):
        raise FileNotFoundError("Le fichier n'existe pas")
    else:
        with open(arg,'r') as file:
            content = file.read()
            with open(args[-1], 'a', encoding='utf-8') as dest_file:
                dest_file.write(content)
                dest_file.write("\n")



    