s = [2,7,12,13]
target = 9
l = 0
r = len(s)-1
while l<r:
    total = s[l]+s[r]
    if total == target:
        print([l+1,r+1])
        break
    elif total < target:
        l+=1
    else:
        r-=1
        
    