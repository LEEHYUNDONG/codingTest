import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[-1]*m for _ in range(n)]
ans = 0

def dfs(x, y, target):
    global ans
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for rx, ry in direction:
        dx, dy = x + rx, y + ry
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] < target:
                visited[x][y]+=dfs(dx, dy, graph[dx][dy])
                
    return visited[x][y]

print(dfs(0, 0, graph[0][0]))