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
            print("True")
        else:
            print("False")
    except ValueError:
        print("This function only takes positive integers")
    
    
