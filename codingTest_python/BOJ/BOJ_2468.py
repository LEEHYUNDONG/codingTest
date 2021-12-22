from collections import deque
import copy
import sys
sys.setrecursionlimit(15000)

n = int(input())
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
graph = [list(map(int, input().split())) for _ in range(n)]
maxV = max(max(graph))
minV = min(min(graph))
answer = []


def dfs(x, y, v):
    if (x < 0) or (x >= n) or (y < 0) or (y >= n):
        return 0
    if tmp[x][y] > v:
        tmp[x][y] = 1   
        dfs(x+direction[0][0], y+direction[0][1], v)
        dfs(x+direction[1][0], y+direction[1][1], v)
        dfs(x+direction[2][0], y+direction[2][1], v)
        dfs(x+direction[3][0], y+direction[3][1], v)
        return 1
    return 0

for k in range(minV, maxV+1):
    tmp = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, k) == 1:
                cnt+=1
    answer.append(cnt)

if max(answer) == 0: 
    print(1)
else:
    print(max(answer))