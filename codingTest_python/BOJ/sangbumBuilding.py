import sys
import copy
from collections import deque

input = sys.stdin.readline

direction = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

def bfs(graph, start):
    q = deque([start]) # level = z, x, y, cnt
    # visited = [[[False] * C]*R for _ in range(L)]
    tmp = copy.deepcopy(graph)
    while q:
        z, y, x, cnt = q.popleft()
        if graph[z][y][x] == 'E':
            return cnt
        for rz, ry, rx in direction:
            dz, dy, dx = z + rz, y + ry, x + rx
            if 0 <= dz < L and 0 <= dx < C and 0 <= dy < R:
                # if not visited[dz][dy][dx] and tmp[dz][dy][dx]!='#':
                if tmp[dz][dy][dx]!='#':
                    q.append([dz, dy, dx, cnt+1])
                    # visited[dz][dy][dx] = True
    # print()
    return None    

ans = []
while True:
    L, R, C = map(int, input().split())
    if L== 0 and R == 0 and C == 0:
        break
    graph = []
    i = 0
    start = []
    while i < L:
        graph.append([])
        for j in range(R+1):
            tmp = list(input().rstrip())
            if tmp == []:
                continue
            for k in range(C):
                if tmp[k] == 'S':
                    start = [k, j, i, 0]
            graph[i].append(tmp)
        i+= 1
    res = bfs(graph, start)
    if res == None:
        ans.append("Trapped!")
    else:
        ans.append("Escaped in "+str(res)+ " minute(s).")

for i in ans:
    print(i)