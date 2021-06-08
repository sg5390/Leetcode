def threeSum(nums):
    a = []
    currnum = 0
    nums.sort()
    for currnum in range(len(nums)-2):  #Instead of using while loop I used for, because while goes infintely and all of the commands would run every single time which is not needed for every statement before while i < j command. 
        if currnum > 0 and nums[currnum] == nums[currnum-1]: #This is done to avoid the repeating numbers from coming in, by increasing the currnum
            continue  #continue makes the program go back to for loop and currnum increases
        i = currnum+1
        j = len(nums)-1
        while i < j:
            sum = nums[currnum] + nums[i] + nums[j]
            if sum == 0:
                a.append([nums[currnum],nums[i],nums[j]])
                while i < j and nums[i] == nums[i+1]: #we are checking whether any of the immediate proceeding numbers are same as nums[i]
                    i += 1 # if they are increase i so that duplicate entries are avoided
                while i < j and nums[j] == nums[j-1]: 
                    j -= 1
                i += 1
                j -= 1
            elif sum < 0:
                i += 1
            elif sum > 0:
                j -= 1

    return a

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(threeSum(nums))