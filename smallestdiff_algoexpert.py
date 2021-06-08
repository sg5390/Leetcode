#O(nlog(n) + O(mlog(m))) | O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    currentdiff = float("inf")
    smallestPair = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        firstnum = arrayOne[idx1]
        secondnum = arrayTwo[idx2]
        if firstnum < secondnum:
            current = secondnum - firstnum
            idx1 += 1
        elif secondnum < firstnum:
            current = firstnum - secondnum
            idx2 += 1
        else:
            return [firstnum, secondnum]
        if smallest > current :
            smallest = current
            smallestPair = [firstnum,secondnum]
    return smallestPair

a1 = [-1,5,10,20,28,3]
a2 = [26,134,135,15,17]
print(smallestDifference(a1,a2))