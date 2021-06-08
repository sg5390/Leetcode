a = [-4,-2,1,3,4,5]
#o/p = [1,4,9,16,16,25]

def sortedSquaredArray(array):
    # Write your code here.
    sortedsquares = [0 for _ in array]
    svi = 0
    lvi = len(array)-1
    for i in reversed(range(len(array))):
        if abs(array[svi]) < abs(array[lvi]):
            sortedsquares[i] = array[lvi] * array[lvi]
            lvi -= 1
        else:
            sortedsquares[i] = array[svi] * array[svi]
            svi += 1
    return sortedsquares

print(sortedSquaredArray(a))