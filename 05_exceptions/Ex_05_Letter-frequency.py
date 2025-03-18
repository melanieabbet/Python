text = open('texte.txt').read()

def letter_counter(text):
    
    Letters = list("abcdefghijklmnopqrstuvwxyz")
    statistic = {letter: 0 for letter in Letters}
    text = text.lower()
    total = 0
    
    for letter in text:
        if letter in Letters:
            statistic[letter] += 1
            total +=1
            
    sorted_statistic = sorted(statistic.items(), key=lambda x: x[1], reverse=True)
    
    
    for letter,count in sorted_statistic:
        try:
            percentage = (count / total *100)
        except ZeroDivisonError:
            percentage = 0
        
        print(f"{letter}: {percentage:.2f}%")
        
letter_counter(text)
        
