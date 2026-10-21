sorted_values  = [1, 3, 5, 8, 12, 15, 20]
target = 7
low = 0
high = len(sorted_values)-1
found= False

while low <= high:
  mid = (low + high) //2
  if target == sorted_values[mid]:
    print(mid)
    found = True
    break
  elif sorted_values[mid]< target:
   low= mid+1    
  else:
   high=mid-1
if not found:
    print("not found")