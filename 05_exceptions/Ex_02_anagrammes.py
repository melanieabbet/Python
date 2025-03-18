words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

anagrams = {}

for word in words:
    word.lower()
    word_sorted = ''.join(sorted(word))
    if word_sorted in anagrams:
        anagrams[word_sorted].append(word)
    else:
        anagrams[word_sorted] = [word]
    
while True:
    
    user_word = input("Entrez un mot: ")
    user_word_sorted = ''.join(sorted(user_word.lower()))

    try:
        user_word_sorted in anagrams
        print(f"Anagrammes trouvés : {anagrams[user_word_sorted]}")
    except KeyError:
        pass       
    if user_word == "":
        print("Au revoir!")
        break



    
