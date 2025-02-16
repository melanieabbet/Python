words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
import random

word = random.choice(words).lower()
word_list = list(word)
print(word)

guessed_list = []
for letter in word_list:
    guessed_list.append("_")
MAX = 5 
allowed_errors = MAX
print(f"Devinez le mot! vous avez droit à {allowed_errors} erreurs")
print(' '.join(guessed_list))
while allowed_errors != 0 and guessed_list != word_list:
    guess = input("Entrez une lettre: ")
    
    if guess in word_list:
        for index, letter in enumerate(word_list) :
            if guess == letter:
                guessed_list[index] = guess           
    else:
        allowed_errors -= 1
        print(f"Non! Plus que {allowed_errors} essais")
    print(' '.join(guessed_list))
if allowed_errors == 0:
    print("Perdu!")
else:
    print("Bravo!")

    




