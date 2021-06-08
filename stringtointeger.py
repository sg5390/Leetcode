class Solution:
    def __init__(self,s):
        self.s = s
    
    def myAtoi(self, s: str) -> int:
        i = 0
        res = 0
        negative = 1
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            i += 1
            negative = -1
        elif i < len(s) and s[i] == '+':
            i += 1

        c = set('0123456789')
        while i < len(s) and s[i] in c:
            res = res * 10 + int(s[i])
            i += 1

        res = res * negative

        if (res < 0):
             return max(res,MIN_INT)   
        return min(res, MAX_INT)

s = Solution("4193 with words")
print(s.myAtoi("4193 with words"))