#cat02.py
def read(filename,item):
    try:
        with open(filename) as filecontent:
            print(filecontent.read(item))
    except FileNotFoundError:
        print("Impossible de trouver le fichier!")

if __name__ == "__main__":
    import sys
    line_number = int(sys.argv[2])
    filename = sys.argv[1]   
    try:
        read(filename, line_number)
    except IndexError:
        print("Arguments manquants")