s = "abcabcbb"

def lengthOfLongestSubstring(s):
    if (s == 0) or (len(s) == 0):
        return 0
    map = {}
    slow = max_len = 0
    li = []
    for fast in range(len(s)):
        c = s[fast]
        
        if c in map:
            slow = max(slow,map[c])
        
        map[c] = fast+1
        current = fast-slow+1
        
        if (current > max_len):
            li = []
            li.append(s[slow:fast+1])
        elif(current == max_len):
            li.append(s[slow:fast+1])
        
        max_len = max(max_len, fast-slow+1)
#             map[s[i]] = i
    # print(li)
    return max_len


print(lengthOfLongestSubstring(s))