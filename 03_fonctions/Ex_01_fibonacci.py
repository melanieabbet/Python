def fibonacci(n):
    list = [1,1]
    print(list[0])
    
    while list[1] < n:
        print(list[1])
        list[0], list[1] = list[1], list[0] + list[1]
        
fibonacci(64)