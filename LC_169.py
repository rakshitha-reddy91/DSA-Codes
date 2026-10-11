nums = [2,2,1,1,1,2,2]
count = 0
candidate = None
for i in nums:
    if count == 0:
        candidate = i
    if i == candidate:
        count += 1
    else:
        count -= 1
print(candidate)