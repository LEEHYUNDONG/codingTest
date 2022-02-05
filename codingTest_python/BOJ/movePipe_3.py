import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
i = 2
dp[0][0][1] = 1

while i < n:
    if graph[0][i] == 1:
        break
    dp[0][0][i] = 1
    i += 1



for i in range(1, n):
    for j in range(2, n):
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] ==0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1] # 대각선과 가로로 부터 온것 더함
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j] # 대각선과 세로로부터 온것 더함

print(sum(dp[i][-1][-1] for i in range(3)))
