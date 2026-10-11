s = "abcabcbb"
seen = set()
max_length =0
l = 0
for r in range(len(s)):
    while s[r] in seen:
        
        seen.remove(s[l])
        l+=1
    seen.add(s[r])
    max_length = max(max_length,r-l+1)
print(max_length)
            
    
    