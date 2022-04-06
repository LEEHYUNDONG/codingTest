import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]
ans = 0

def dfs(x, y, visited):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for dx, dy in directions:
        rx = x + dx
        ry = y + dy
        if 0<= rx < n and 0 <= ry < m:
            if graph[x][y] > graph[rx][ry]:
                visited[x][y] += dfs(rx, ry, visited)
    
    return visited[x][y]

dfs(0, 0, visited)

print(visited[0][0])