words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]



while True:
    user_word = input("Entrez un mot: ")
    letter_list = list(user_word)
    for word in words:
        if all(letter in word.lower() for letter in letter_list[:]):
            print(word)
        else:
            break
    