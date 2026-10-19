nums =[7,4,84,12,65,1,39,27,99,108,77]

for i in range(len(nums)):
  for j in range(len(nums)-1-i):
    if nums[j]> nums[j+1]:
      nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)