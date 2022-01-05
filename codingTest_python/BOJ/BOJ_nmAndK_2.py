import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

dx = [-1, 1, 1, -1, -2, 2, 0, 0]
dy = [-1, 1, -1, 1, 0, 0, 2, -2]
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = -100000


def dfs(x, y, tot, depth):
    global ans
    if visited[x][y]:
        return
    if depth == k:
        ans = max(tot, ans)
        return
    visited[x][y] = True
    for i in range(8):
        rx = x + dx[i]
        ry = y + dy[i]
        if 0 <= rx < n and 0 <= ry < m:
            dfs(rx, ry, tot + graph[rx][ry], depth+1)


for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        dfs(i, j, graph[i][j], 1)

print(ans)
