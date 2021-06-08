def missingNumber(nums):
    #O(n) | O(1) : Using XOR operation
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

    #O(n) | O(n) : Using a Hashset
    numset = set(nums)
    print(numset)
    n = len(nums)+1
    for i in range(n):
        if i not in numset:
            return i





    #O(nlogn) | O(1) bcz we sorted nums in place, if we sort nums in a diff array space = O(n)
    nums.sort()
    for i in range(len(nums)):
        if i == nums[i]:
            i += 1
        else:
            return i
    return 1 if len(nums) == i-1 else i

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))