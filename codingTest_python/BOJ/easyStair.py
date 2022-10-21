N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]
MOD = 1000000000

print(dp)


for i in range(1, 10):
    dp[0][i] = 1



for i in range(1, N):
    for j in range(1, 10):
        if j == 9:
            dp[i][j] = (dp[i-1][j-1])%MOD
        elif j == 1:
            dp[i][j] = (dp[i-1][j+1]+1)%MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%MOD

    
print(dp[N-1])
print(sum(dp[N-1]))

