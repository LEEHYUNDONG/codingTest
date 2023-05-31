import sys
import copy
from collections import deque
input = sys.stdin.readline


# 안전 영역 3군데 dfs로 정하기 - 브루트포스
def dfs(graph, virus, cnt):
    global ans

    if cnt == 3:
        ttmp = copy.deepcopy(graph)
        tmp = 0
        for i in range(len(virus)):
            spread(virus[i][0], virus[i][-1], ttmp)
        
        for i in range(N):
            for j in range(M):
                if ttmp[i][j] == 0:
                    tmp += 1
        ans = max(tmp, ans)
        return graph
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(graph, virus, cnt+1)
                graph[i][j] = 0

# 바이러스 퍼뜨리기
def spread(x, y, graph):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0,1):
        rx, ry = x + dx, y + dy
        if 0<= rx < N and 0<= ry < M:
            if graph[x][y] == 2 and graph[rx][ry] == 1:
                continue
            elif graph[x][y] == 2 and graph[rx][ry] == 0:
                graph[rx][ry] = 2
                spread(rx, ry, graph)


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
virus = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i, j])


dfs(graph, virus, 0)
print(ans)