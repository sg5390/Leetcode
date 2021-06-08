arr1 = [1,2,4,5,11]
target1 = 9

arr2 = [3,3]
target2 = 6

def two_sum(nums, target):
        maps = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if nums[i] in maps:
                return [maps[nums[i]],i]
            else:
                maps[a] = i
                
list1 = two_sum(arr1,target1)
print(list1)

list2 = two_sum(arr2,target2)
print(list2)
