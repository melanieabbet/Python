import math

def debug(f, *args):
    print(f"Calling {f} with args {args}")
    result = f(*args)
    print(f"The result is {result}")
    return result

def debug2(f):
    def intern(*args):
        print(f"Calling {f} with args {args}")
        result = f(*args)
        print(f"The result is {result}")
        return result
    return intern

# pourquoi "and kwargs {}" dans le rendu demandé?
