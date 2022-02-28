import sys
import copy
from collections import deque

input = sys.stdin.readline

direction = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

def bfs(graph, start):
    q = deque([start]) # level = z, x, y, cnt
    visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = 0
    while q:
        z, x, y = q.popleft()
        for rz, rx, ry in direction:
            dz, dy, dx = z + rz, y + ry, x + rx
            if 0 <= dz < L and 0 <= dx < R and 0 <= dy < C:
                if graph[dz][dx][dy] == 'E':
                    return visited[z][x][y] +1
                if visited[dz][dx][dy] == -1 and graph[dz][dx][dy] == '.':
                    visited[dz][dx][dy] = visited[z][x][y] + 1
                    q.append([dz, dx, dy])
    return None    

ans = []
while True:
    L, R, C = map(int, input().split())
    if L== 0 and R == 0 and C == 0:
        break
    graph = [[[]*C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        graph[i] = [list(input()) for _ in range(R)]
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    res = bfs(graph, [i, j, k])
                    if res == None:
                        ans.append("Trapped!")
                    else:
                        ans.append("Escaped in "+str(res)+ " minute(s).")
                    break


for i in ans:
    print(i)