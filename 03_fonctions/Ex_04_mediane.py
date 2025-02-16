def mediane(*args):
    list = sorted(args)
    lenght = len(list)
    
    if lenght%2 == 0:
        result = (list[((lenght-1)//2)] + list[(lenght//2)]) / 2
    else:
        result = list[(lenght)//2]
    return result
    
print("Entrez un nombre par ligne, ligne vide pour terminer.")
user_list =[]
while True:
    number = input()
    if number == "":
        print(f"Vous avez entré {len(user_list)} nombres; leur mediane est {mediane(*user_list)}")
        break
    user_list.append(int(number))