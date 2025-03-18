import sys

if len(sys.argv) < 5:
    print('Vous devez fournir 4 arguments')

try:
    with open(sys.argv[1], 'r') as input:     
        try:
            with open(sys.argv[2], 'x') as output:
                for el in input:
                    modified_el = el.replace(sys.argv[3],sys.argv[4])
                    output.write(modified_el)
        except FileExistsError:
            print("File already existing")
            sys.exit(1)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

#python search_replace.py input.txt output.txt "Monica" "Maman" 


