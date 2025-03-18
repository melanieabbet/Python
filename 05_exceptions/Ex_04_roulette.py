

def roulette_simple():
    x = 0
    try:
        while True:
            if x < 9:
                x += 1
                print(x)
            else:
                x = 0
    except KeyboardInterrupt:
        print(f"stopped at {x}")

        
        
def roulette_composed():
    x = y = z = 0
    try:
        while True:
            x += 1
            y += 1
            z += 1
            
            if x == 9:
                x = 0
            if y == 10:
                y = 0
            if z == 11:
                z = 0
                
    except KeyboardInterrupt:
        if x == y == z:
            print(f"Gagné ! {x} - {y} - {z}")
        else:
            print(f"Perdu ! {x} - {y} - {z}")