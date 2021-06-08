a = [5,1,22,25,6,-1,8,10]
seq = [1,6, -1, 10]

def isValidSubsequence(array, sequence):
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)
           


print(isValidSubsequence(a,seq))