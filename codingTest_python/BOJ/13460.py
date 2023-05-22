

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
red = []
blue = []


for i in range(N):
    for j in range(M):
        if graph[i][j] =='R':
            graph[i][j] = '.'
            red = [i, j]
        if graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = [i, j]

