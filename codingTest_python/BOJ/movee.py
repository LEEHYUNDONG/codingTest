import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = graph[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1]+graph[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j]+graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], max(dp[i-1][j-1], dp[i][j-1])) + graph[i][j]

print(dp[-1][-1])