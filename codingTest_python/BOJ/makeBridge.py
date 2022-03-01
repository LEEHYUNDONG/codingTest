import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j):
    q = deque([[i, j]])
    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    tmp = int(1e9)
    while q:
        x, y = q.popleft()
        for rx, ry in direction:
            dx, dy = x + rx, y + ry
            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] == 0 and graph[dx][dy] == 0:
                    q.append([dx, dy])
                    visited[dx][dy] = visited[x][y] + 1
                if graph[dx][dy] == 1:
                    flag = True
                    for tx, ty in direction:
                        dtx, dty = dx + tx, dy + ty
                        if 0 <= dtx < n and 0 <= dty < n:
                            if i == dtx and j == dty:
                                flag = False
                                break
                        else:
                            flag = False
                            continue
                    if flag:
                        tmp = min(tmp, visited[x][y])
                
                    
    return tmp+1

res = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            for rx, ry in direction:
                ddx, ddy = i+rx, j+ry
                if 0 <= ddx < n and 0 <= ddy < n:
                    if graph[ddx][ddy] == 0:
                        # print(ddx, ddy)
                        res = min(res, bfs(ddx, ddy))
print(res)
