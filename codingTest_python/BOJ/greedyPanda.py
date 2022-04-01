import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dp = [[-1]*n for _ in range(n)]
ans = 0

def dfs(x, y):
    global ans
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            rx, ry = x + dx[i], y + dy[i]
            if 0 <= rx < n and 0 <= ry < n and graph[rx][ry] > graph[x][y]:
                dp[x][y] = max(dp[x][y], dfs(rx, ry))
                
    return dp[x][y] + 1




for i in range(n):
    for j in range(n):
        ans = max(dfs(i, j), ans)
                

print(ans)