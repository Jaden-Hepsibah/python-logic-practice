a= int(input("Enter a number A: "))
b= int(input("Enter a number B: "))

if(a==b==1 or a==1):
    gcd= 1
else:
  for candidate in range (1, min(a,b)+1, 1):
    if a% candidate ==0 and b% candidate==0:
      gcd=candidate
print("greatest common divisor of (a,b) is",gcd)
LCM = (a*b//gcd)
print("the least common divisor of (a,b) is", LCM)