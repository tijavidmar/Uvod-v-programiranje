def fibo(n):
    
    # bazna primera
    if n <= 2:
        return 1  # fibo(1) = fibo(2) = 1
    
    else:
        # rekurzivni korak
        return fibo(n - 1) + fibo(n - 2)  # komentar na koncu
    
