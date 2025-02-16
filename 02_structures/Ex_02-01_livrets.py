import random

while True:
    x = random.randint(1,9)
    y= random.randint(1,9)

    while (i := int(input(f'{x} x {y} = ')) != x*y):
        print("Non, ré-essayez !")
    print("Bravo!")
