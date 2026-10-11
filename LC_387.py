s = "loveleetcode"
result = -1
for i in range(len(s)):
    if s.count(s[i]) == 1:
        result = i
        break

print(result)
