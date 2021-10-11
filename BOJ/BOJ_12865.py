n, k = map(int, input().split())
sack = [list(map(int, input().split())) for _ in range(n)]
INF = -int(1e9)

dp = [INF for _ in range(k+1)]
dp[0] = 0

for i in range(1, k+1):
    for w, v in sack:
        if i > w:
            dp[i] = max(dp[i], dp[w]+dp[i-w])
        else:
            dp[w] = v
print(dp[k])
