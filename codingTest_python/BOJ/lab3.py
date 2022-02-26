import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline
n, vir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
direction = [(0,1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j, 0])

def bfs(vv):
    q = deque(list(vv))
    tmp = copy.deepcopy(graph)
    visited = [[0]*n for _ in range(n)]
    time = 0
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = 1
        for rx, ry in direction:
            dx, dy = x + rx, y + ry
            if 0 <= dx < n and 0 <= dy < n:
                if tmp[dx][dy] == 1:
                    visited[dx][dy] = 1
                    continue
                if not visited[dx][dy] and tmp[dx][dy] != 1:
                    visited[dx][dy] = 1
                    if tmp[dx][dy] == 0:
                        tmp[dx][dy] = 2
                        time = cnt+1
                    q.append([dx, dy, cnt+1])
                
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 0:
                return None
    return time


ans = int(1e9)
res = 0
for i in combinations(virus, vir):
    res = bfs(i)
    if res != None:
        ans = min(res, ans)

print(ans) if ans != int(1e9) else print(-1)