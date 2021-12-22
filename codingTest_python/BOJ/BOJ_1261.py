# 알고스팟
from collections import deque
m, n = map(int, input().split())
INF = int(1e9)
graph = [input() for i in range(n)] 
rx = [1, -1, 0, 0]
ry = [0, 0, 1, -1]
distance = [[-1]*m for _ in range(n)]

def dijkstra(i, j):
    q = deque()
    q.append([0, 0])
    distance[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x+rx[i], y+ry[i]
            if 0 <= dx and dx < n and 0 <= dy and dy < m:
                if distance[dx][dy] == -1:
                    if graph[dx][dy] == '0':
                        q.appendleft([dx, dy])
                        distance[dx][dy] = distance[x][y]
                    elif graph[dx][dy] == '1':
                        q.append([dx, dy])
                        distance[dx][dy] = distance[x][y] + 1
                    
dijkstra(0, 0)
print(distance[n-1][m-1])