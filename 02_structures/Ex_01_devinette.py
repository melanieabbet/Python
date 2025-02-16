import random
random_number = random.randint(1,10)
print("Devinez un nombre entre 1 et 10")
#print(random_number)

user_guess = int(input("Votre proposition:"))

while user_guess != random_number:
    if user_guess < random_number:
        print("Non, plus!")
        user_guess = int(input("Votre proposition:"))
    elif user_guess > random_number:
        print("Non, moins!")
        user_guess = int(input("Votre proposition:"))
print("Bravo!")
        