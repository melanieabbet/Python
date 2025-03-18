#cat03.py
def read(filename):
    try:
        with open(filename) as f:
            for l in f:
                print(l)
    except FileNotFoundError:
        print("Impossible de trouver le fichier!")

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]   
    try:
        read(filename)
    except IndexError:
        print("Arguments manquants")