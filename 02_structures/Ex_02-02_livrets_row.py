import random
guessed = 0

while guessed < 5:
    x = random.randint(1,9)
    y= random.randint(1,9)

    while (i := int(input(f'{x} x {y} = ')) != x*y):
        print("Non, ré-essayez !")
        guessed = 0
    print("Bravo!")
    guessed += 1