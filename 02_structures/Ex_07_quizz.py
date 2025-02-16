import random

print("Préparation du quizz")
quizz =[]

while True:
    question = input("Question (<enter> pour terminer):")
    if question == "":
        break
    answer = input("Réponse: ")
    quizz.append((question,answer))


print("Début du quizz!")

while quizz:
    random.shuffle(quizz)
    for question in quizz:
        print(question[0])
        answer = input( "> ")
        if answer == question[1]:
            print("Oui!")
            quizz.remove((question))
        else:
            print("Non!")
