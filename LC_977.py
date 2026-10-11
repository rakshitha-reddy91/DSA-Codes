nums = [-4,-1,0,3,10]
s = []
for i in range(len(nums)):
    nums[i] = nums[i]**2
    s.append(nums[i])
    s.sort()
print(s)