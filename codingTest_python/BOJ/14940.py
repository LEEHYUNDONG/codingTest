from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
answer = [[-1]*M for _ in range(N)]


def bfs(graph, sx, sy):
    visited = [[0]*M for _ in range(N)]
    dq = deque([[sx, sy]])
    visited[sx][sy] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            rx, ry = x + dx[i], y + dy[i]
            if 0 > rx or rx >= N or 0 > ry or ry >= M or graph[rx][ry] == 0:
                continue
            if visited[rx][ry] == 0 and graph[rx][ry] == 1:
                visited[rx][ry] = visited[x][y] + 1
                dq.append([rx, ry])
    
    return visited
    


for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            answer = bfs(graph, i, j)
            answer[i][j] = 0
        
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and answer[i][j] == 0:
            answer[i][j] = -1


for i in range(N):
    print(*answer[i])