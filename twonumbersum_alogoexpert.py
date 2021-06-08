array1 = [3,5,4,8,11,1,-1,6,5,14]
targetSum1 = 10

def twoNumberSum(array, targetSum):
#Using Dictionary/Hash Map:
    dict = { }
    a = []
    for i in array:
        diff = targetSum - i
        if diff in dict:
            a.append([diff,i])
        else:
            dict[i] = True

    return a

#Using two pointer approach
    # array.sort()
    # currentSum = 0
    # left = 0
    # right = len(array) - 1
    # while left < right:

    #     currentSum = array[left] + array[right]
    #     print("currentSum", currentSum)
    #     if currentSum == targetSum:
    #         return [array[left],array[right]]
    #     elif currentSum < targetSum:
    #         left += 1
    #     elif currentSum > targetSum:
    #         right -= 1
    # return []


#Using array
    # a = []
    # for i in array:
    #     diff = targetSum - i
    #     if diff not in array:
    #         pass
    #     else:
    #         if diff != i and i not in a:
    #             a.append(diff)
    #             a.append(i)
    # return a
    
print(twoNumberSum(array1,targetSum1))