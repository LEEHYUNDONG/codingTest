#1904 01타일
n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if i == 1:
        dp[i] = dp[i-1]
        continue
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n])
