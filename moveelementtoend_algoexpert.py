def moveElementToEnd(array, toMove):
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left],array[right] = array[right],array[left]
            right -= 1
            left += 1
        elif array[right] == toMove:
            right -= 1
        else:
            left += 1
    return array


array = [2,1,2,2,2,3,4,2]
toMove = 2
print(moveElementToEnd(array, toMove))
