words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

words_sorted = []
for word in words:
    word.lower()
    words_sorted.append(''.join(sorted(word)))
    
while True:
    user_word = input("Entrez un mot: ")
    user_word_sorted = ''.join(sorted(user_word.lower()))
    print(user_word_sorted)

    for index, word in enumerate(words_sorted) :
        if word == user_word_sorted:
            print(words[index])
            #print(words[words_sorted.index(word)])
    if user_word == "":
        print("Au revoir!")
        break



    
