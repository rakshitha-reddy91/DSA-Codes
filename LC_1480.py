nums = [1,2,3,4,5]
for i in range(1,len(nums)):
    nums[i]= nums[i]+nums[i-1]
print(nums)    