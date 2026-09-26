n= int(input("Enter a number: "))
count=0
for i in range(1,n+1):
  if(n%i==0):
    count+=1

if count > 2:
  print("its not a prime number")
elif (n==1):
  print("1 is neither prime nor composite")
else:
  print("its prime number")