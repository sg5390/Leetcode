from collections import defaultdict

#def groupAnagrams(strs):
ans = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]
for i in strs:
    a = tuple(sorted(i))
    print(a)
    ans[a].append(i)
print(ans)
    



# print(groupAnagrams(strs))