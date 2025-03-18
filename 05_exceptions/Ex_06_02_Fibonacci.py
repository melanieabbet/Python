def fibonacci_checker(n):
    list = [1,1]
    results = []

    try:
        n = int(n)
        if n<=0:
            raise ValueError("This function only takes positive integers")
        
        while list[1] <= n:
            results.append(list[1])
            list[0], list[1] = list[1], list[0] + list[1]
            
        if n in results:
            return True
        else:
            return False
    except ValueError:
        print("This function only takes positive integers")
    
while i := input("Entrez une valeur (vide pour quitter):"):
    
    try:
        i = int(i)
        if i<= 0:
            raise ValueError
        is_fibonacci = fibonacci_checker(i)
    except ValueError:
        print("Entrez un nombre entier")
        continue
    
    if is_fibonacci:
        print(f"{i} est dans la suite de Fibonacci")
    else:
        print(f"{i} n'est pas dans la suite de Fibonacci")
print("Au revoir")      
    
