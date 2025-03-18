def typed_input(user_input, type=int):
    while True:
        try:
            return type(input(user_input))
        except ValueError:
            print(f"Entrée invalide, type attendu: {type}")
    
test_nombre = typed_input("Entrez un nombre entier : ")
print("Vous avez entré :", test_nombre)
test_float = typed_input("Entrez un nombre décimal : ",float)
print("Vous avez entré :", test_float)
test_text = typed_input("Entrez du text : ",str)
print("Vous avez entré :", test_text)