import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
ans = -1
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x, y):
    q = deque([[x, y]])
    visited = [[-1]*m for _ in range(n)]
    visited[x][y] = True
    tmp = -1
    while q:
        x, y = q.popleft()
        for rx, ry in direction:
            dx, dy = rx+x, ry+y
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == -1 and graph[dx][dy] == 'L':
                    q.append([dx,dy])
                    visited[dx][dy] = visited[x][y]+1
                    tmp = max(visited[dx][dy], tmp)
    return tmp-1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(bfs(i, j), ans)
print(ans)