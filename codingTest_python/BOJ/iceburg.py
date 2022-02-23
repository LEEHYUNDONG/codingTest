import sys, copy
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    visited[x][y] = True
    for rx, ry in direction:
        dx, dy = x + rx, y + ry
        if 0 <= dx < n and 0 <= dy < m:
            if not visited[dx][dy] and graph[dx][dy] != 0:
                dfs(dx, dy)
    
    return 1
ice = deque([])
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] != 0:
            ice.append([i, j])
    graph.append(tmp)

res = 0
flag = True

while ice:
    frag = 0
    tmp = copy.deepcopy(graph)

    for i in range(len(ice)):
        x, y = ice.popleft()
        cnt = 0
        for rx, ry in direction:
            dx, dy = x + rx, y + ry
            if 0 <= dx < n and 0 <= dy < m:
                if tmp[dx][dy] == 0:
                    cnt += 1
        graph[x][y] -= cnt
        if graph[x][y] <= 0:
            graph[x][y] = 0
            continue
        ice.append([x, y])
    visited = [[False]*m for _ in range(n)]
    res += 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                print("i, j :", i, j)
                frag += dfs(i, j)
    
    if frag >= 2:
        print(res)
        flag = False
        break

if flag:
    print(0)