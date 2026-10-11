from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
group = defaultdict(list)
for word in strs:
    
    key = ''.join(sorted(word))
    group[key].append(word)
print(list(group.values()))