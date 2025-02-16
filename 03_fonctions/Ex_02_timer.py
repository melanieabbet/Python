import time
def countdown(n=10):
    while n > 0:
        print(f"Il reste {n} secondes.")
        n -= 1
        time.sleep(1)
        
countdown() 
    