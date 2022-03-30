import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]
sX, sY, eX, eY = map(int, input().split())
sX, sY, eX, eY = sX-1, sY-1, eX-1, eY-1

ans = int(1e9)
q = deque([])
q.append([sX, sY])
visited = [[int(1e9)]*m for _ in range(n)]
visited[sX][sY] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        rx, ry = x, y
        rx += dx[i]
        ry += dy[i]
        wide = 1
        while wide <= k and 0 <= rx < n and 0 <= ry < m and field[rx][ry] == '.' and visited[rx][ry] > visited[x][y]:
            if visited[rx][ry] == int(1e9):
                q.append([rx, ry])
                visited[rx][ry] = visited[x][y] + 1
            rx += dx[i]
            ry += dy[i]
            wide += 1


if visited[eX][eY] == int(1e9):
    print(-1)
else:
    print(visited[eX][eY])
