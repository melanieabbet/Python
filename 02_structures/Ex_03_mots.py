words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]

#print(words)
print(f"Nombre de mots: {len(words)}")

four_letter_words = 0
z_words =0
start_a_finish_s_word = 0
words_containing_z =  0

for word in words:
    if len(word) == 4:
        four_letter_words += 1
    if word.lower().startswith('z'):
        z_words += 1
    if word.lower().startswith('a') and word.endswith('s'):
        start_a_finish_s_word += 1
    if "z" in word.lower():
        words_containing_z += 1
        #print(word)
print(f"Nombre de mots de quatre lettres: {four_letter_words}")
print(f"Nombre de mots commençant par z: {z_words}")
print(f"Nombre de mots commençant par a et terminant par s: {start_a_finish_s_word}")
print(f"Nombre de mots contenant z: {words_containing_z}")


