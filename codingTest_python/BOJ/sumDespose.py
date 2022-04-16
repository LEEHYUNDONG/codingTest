N, K = map(int, input().split())

dp = [0 for _ in range(N+1)]
mod = 1000000000

dp[0] = 1

for _ in range(K):
    for i in range(1, N+1):
        dp[i] = (dp[i]+dp[i-1]) % mod

print(dp[N])

