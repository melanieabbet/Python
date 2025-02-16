import random
MAX = 2
questions=[]
guessed=[]

for number_one in range(1,MAX+1):
    for number_two in range(number_one,MAX+1): 
        questions.append((number_one,number_two))
        
while questions:
    question = random.choice(questions)
    
    while (i := int(input(f'{question[0]} x {question[1]} = ')) != question[0]*question[1]):
        print("Non, Ré-essayons")
    print("Bravo!")
    questions.remove(question)
    guessed.append(question)
    #print(guessed)
    


#print(questions)

