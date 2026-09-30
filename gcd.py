def fun (a,b):
    if b==0:
        return a
    else:
        return fun(b, a%b)

a= int(input("Enter a number A: "))
b= int(input("Enter a number B: "))
print("GCD of", a, "and", b, "is:", fun(a, b))
