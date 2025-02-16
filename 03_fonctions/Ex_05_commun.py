#common("chien","chat")

def common(a,b):
    set_a = set(a)
    set_b = set(b)
    items = set_a & set_b
    return items

def common2(a,b):
    items = []
    for letter in a:
        if letter in b and letter not in items:
            items.append(letter)
    return items

#tests
import timeit
word1=input("word1 = ")
word2=input("word2 = ")

print(timeit.timeit('common(word1, word2)', globals=globals()))
print(timeit.timeit('common2(word1, word2)', globals=globals())) #plus rapide

