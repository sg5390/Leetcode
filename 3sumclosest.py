def threeSumClosest(nums,target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            currsum = nums[i]+nums[left]+nums[right]
            if abs(currsum - target) < abs(res - target):
                res = currsum
            if currsum < target:
                left += 1
            else:
                right -= 1
    return res


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums,target))








    a = dict()
    currnum = 0
    nums.sort()
    for currnum in range(len(nums)-2):  #Instead of using while loop I used for, because while goes infintely and all of the commands would run every single time which is not needed for every statement before while i < j command. 
        if currnum > 0 and nums[currnum] == nums[currnum-1]: #This is done to avoid the repeating numbers from coming in, by increasing the currnum
            continue  #continue makes the program go back to for loop and currnum increases
        i = currnum+1
        j = len(nums)-1
        dictindx = 0
        while i < j:
            sum = nums[currnum] + nums[i] + nums[j]
            diff = target - sum
            if sum == target:
                a[dictindx] = diff
                print(a)
                while i < j and nums[i] == nums[i+1]: #we are checking whether any of the immediate proceeding numbers are same as nums[i]
                    i += 1 # if they are increase i so that duplicate entries are avoided
                while i < j and nums[j] == nums[j-1]: 
                    j -= 1
                i += 1
                j -= 1
                dictindx += 1
            elif sum < target:
                i += 1
                a[dictindx] = diff
                print(a)
                dictindx += 1
            elif sum > target:
                j -= 1
                a[dictindx] = diff
                print(a)
                dictindx += 1
    return min(a,key = a.get)


