# https://www.acmicpc.net/status?user_id=easttwave&problem_id=16930&from_mine=1
import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]
startX, startY, endX, endY = map(int, input().split())
startX -= 1
startY -= 1
endX -= 1
endY -= 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[int(1e9)]*m for _ in range(n)]

def bfs(startX, startY):
    global ans
    q = deque([])
    q.append([startX, startY])
    visited[startX][startY] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            wide = 1
            while wide <= k and 0 <= rx < n and 0 <= ry < m and field[rx][ry] =='.' and visited[rx][ry] > visited[x][y]:
                if visited[rx][ry] == int(1e9):
                    visited[rx][ry] = visited[x][y] + 1
                    q.append([rx, ry])
                rx += dx[i]
                ry += dy[i]
                wide += 1



bfs(startX, startY)
if visited[endX][endY] == int(1e9):
    print(-1)
else:
    print(visited[endX][endY])
