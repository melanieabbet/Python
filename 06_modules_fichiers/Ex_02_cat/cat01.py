#cat01.py
def read(filename):
    try:
        with open(filename) as filecontent:
            print(filecontent.read())
    except FileNotFoundError:
        print("Impossible de trouver le fichier!")

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    try:
        read(args[0])
    except IndexError:
        print("Nom de fichier manquant")