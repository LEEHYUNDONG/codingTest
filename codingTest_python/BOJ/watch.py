import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))
cctv = deque([])
graph = [list(map(int, input().split())) for _ in range(n)]
mode = [
    [[0], [1], [2], [3]], 
    [[0,2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
direction = [(1,0), (-1,0), (0, 1), (0, -1)] #하, 상, 우, 좌

for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] <= 5:
            cctv.append([graph[i][j], i, j])


def dfs(x, y, type):
    
    for i in range(4):
        if not visited[x][y]:
            visited[x][y] = True
        