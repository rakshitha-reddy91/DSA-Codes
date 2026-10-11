nums = [0,1,0,12,13]
k = 0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[k]=nums[k],nums[i]
        k+=1
print(nums)