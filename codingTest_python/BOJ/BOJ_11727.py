n = int(input())
dp = [0] * (n+1)

for i in range(n+1):
    if i == 1 or i == 0:
        dp[i] = 1
        continue
    dp[i] = (dp[i-1]+dp[i-2]*2)%10007

print(dp[n])