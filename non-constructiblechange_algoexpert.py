def nonConstructibleChange(coins):

#COME BACK TO THIS PROBLEM AGAIN

# Write your code here.
    c = 0
    coins.sort()
    for coin in coins:
        if coin > c + 1:
            return c + 1
        else:
            c += coin
    return c + 1


coins = [5,7,1,1,2,3,22]
print(nonConstructibleChange(coins))