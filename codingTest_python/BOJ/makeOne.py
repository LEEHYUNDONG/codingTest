n = int(input())

dp = [0 for _ in range(1000001)]
seq = [[] for _ in range(1000001)]

dp[1]= 0
seq[1] = [1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    seq[i] = seq[i-1] + [i]

    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        seq[i] = seq[i//3] + [i]
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        seq[i] = seq[i//2] + [i]
    
seq[n].sort(reverse=True)
print(dp[n])
print(*seq[n])