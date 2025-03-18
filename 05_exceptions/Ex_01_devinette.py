import random
random_number = random.randint(1,10)
print("Devinez un nombre entre 1 et 10")
#print(random_number)

user_guess = input("Votre proposition:")

while user_guess != random_number:
    try:
        user_guess = int(user_guess)
    except ValueError:
        print('Entrée invalide - chiffre entier attendu')
    else:
        if user_guess < random_number:
            print("Non, plus!")
        if user_guess > random_number:
            print("Non, moins!")
        if user_guess == random_number:
            print("Bravo!")
            break
    user_guess = input("Votre proposition:")   

        
