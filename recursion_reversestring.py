def reverseString(s):
    new_arr = []
    n = len(s)
    for i in reversed(s):
        # print(i)
        new_arr.append(i)
        # print(new_arr)
    return new_arr


s = ['h','e','l','l','o']
print(reverseString(s))