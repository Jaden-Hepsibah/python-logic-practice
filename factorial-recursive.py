def fun(n):
    if n<=1:
        return 1
    else:
        return n*fun(n-1)
    
print("Factorial of 5 is:", fun(5))