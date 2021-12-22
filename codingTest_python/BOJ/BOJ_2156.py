n = int(input())
dp = [0]*(n+1)
wine = [0]
for i in range(n):
    wine.append(int(input()))

dp[0] = wine[0]
dp[1] = wine[1]

if n > 1:
    dp[2] = wine[2] + wine[1]

for i in range(3, len(wine)):
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
    dp[i] = max(dp[i-1], dp[i])

print(dp[n])
