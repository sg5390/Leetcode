def strStr(haystack, needle):
    s = []
    i = 0
    j = 0
    while i < len(haystack) and j < len(needle):
        if haystack == "" or len(haystack) == 0:
            return 0
        if(haystack[i:] == needle[0]):
            return i
        i += 1
        if(haystack[i] != needle[0] and i = len):
            return -1
    


haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))