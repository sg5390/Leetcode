a = set()
#a.add()

nums = ['4','13','5','/','+']
stack = []  #[2,4,6]
for i in range(len(nums)):
    if (nums[i] != '/' or '+' or '-' or '*'):
        stack.append(int(nums[i]))
    else:
        first = stack.pop() #5 
        second = stack.pop() #13
        if nums[i] == '-':
            stack.append(second - first)
        elif nums[i] == '*':
            #div = second / first
            stack.append(second * first)
        elif nums[i] == '+':
            #div = second / first
            stack.append(second + first)
        else:
            #div = second / first
            stack.append(second / first)

return stack.pop()
