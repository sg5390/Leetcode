map = {}
for i in nums:
    if i in map:
        return True
    else:
        map[i] = 1
return False

# hashset = set()
#         for i in nums:
#             if i in hashset:
#                 return True
#             else:
#                 hashset.add(i)
#         return False