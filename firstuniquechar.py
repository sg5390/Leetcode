O(n) | O(1)


import collections
s = "loveleetcode"

def firstUniqChar(s):
    a = collections.Counter(s)
    for i,char in enumerate(s):
        if a[char] == 1:
            return i 
    return -1
  
print(firstUniqChar(s))