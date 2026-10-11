nums = [2,7,11,15]
target = 9
seen = {}
for i in range(len(nums)):
    c=target-nums[i]
    if c in seen:
        print(seen[c],i)
        break
    seen[nums[i]] =i