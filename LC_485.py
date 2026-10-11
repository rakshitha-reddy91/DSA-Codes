s = [1,1,0,1,1,1,1]
c = 0
max_v = 0
for i in s:
    if i == 1:
        c+=1
        max_v=max(max_v,c)
    else:
        c = 0
print(max_v)