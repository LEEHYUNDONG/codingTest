import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, graph):
    q = deque([[x, y]])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] += 1
    while q:
        x, y = q.popleft()
        for rx, ry in direction:
            dx, dy = x + rx, y + ry
            if 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] == 0 and visited[dx][dy] == 0:
                    q.append([dx, dy])
                    visited[dx][dy] += 1
                if graph[dx][dy] == 1:
                    visited[dx][dy] += 1
    return visited

hour = 0
while True:
    flag = False
    
    ch = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                ch = bfs(0, 0, graph)
                flag = True
                break
    if not flag:
        print(hour)
        break
    for i in range(n):
        for j in range(m):
            if ch[i][j] >= 2:
                graph[i][j] = 0
    hour += 1