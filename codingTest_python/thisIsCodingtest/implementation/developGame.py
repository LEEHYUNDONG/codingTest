import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*m for _ in range(n)]
direction = 0
r, c, direction = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
q = deque([[r, c, direction]])
cnt = 0
graph[r][c] = 1
flag = 0

while q:
    x, y, d = q.popleft()
    for i in range(1, 5):
        rx = dx[(d-i) % 4] + x
        ry = dy[(d-i) % 4] + y
        if 0 <= rx < n and 0 <= ry < m and graph[rx][ry] == 0:
            graph[rx][ry] = 1
            q.append([rx, ry, (d-i) % 4])
            cnt += 1
            flag = 0
        else:
            flag += 1
    if flag == 4:
        x -= dx[(d-i) % 4]
        y -= dy[(d-i) % 4]
        if graph[x][y] == 1:
            break
        else:
            q.append([x, y, (d-i) % 4])

print(cnt)
