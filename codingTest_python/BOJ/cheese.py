import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
cheese = deque([])
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False]*m for _ in range(n)]
hour = 0
cnt = 0
def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    # 한번 while문 끝날 때마다 1시간 지난다.
    while q:
        x,y = q.popleft()
        for rx, ry in direction:
            nx = x + rx
            ny = y + ry
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    
    return cnt

while True:
    hour += 1
    tmp = 0
    visited = [[False]*m for _ in range(n)]
    tmp = bfs()
    if tmp == 0:
        break
    cnt = tmp
print(hour-1)
print(cnt)