# mediane.py

def mediane(*args):
    my_list = sorted(args)
    my_lenght = len(my_list)
    
    if my_lenght%2 == 0:
        result = (my_list[((my_lenght-1)//2)] + my_list[(my_lenght//2)]) / 2
    else:
        result = my_list[(my_lenght)//2]
    return result

if __name__ == "__main__":

    import sys
    args = list(map(int, sys.argv[1:]))
    print(mediane(*args))