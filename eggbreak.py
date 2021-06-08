def superEggDrop(k,n):
    dp = [[]*(k+1),[]*(n+1)]
    for j in range(len(dp[0])):   #Length of columns
        dp[1][j] = j
    for i in range(2,len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = float("inf")
            for f in range(len(j)):
                dp[i][j] = min(dp[i][j],1+max(dp[i-1][f-1],dp[i][j-f]))
    return dp

k= 3
n = 14
print(superEggDrop(k,n))