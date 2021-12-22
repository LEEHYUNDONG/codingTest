# 평범한 배낭
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
dx = [-1, 1, 0, 0]
dy =  [0, 0, -1, 1]
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False ] * n for _ in range(n)] 

def dfs(a, b):
    visited[a][b] = True
    color = graph[a][b]
    for i in range(4):
        rx = dx[i] + a
        ry = dy[i] + b
        if (0 <= rx < n) and (0 <= ry < n):
            if visited[rx][ry] == False:
                if graph[rx][ry] == color:
                    dfs(rx, ry)  

cnt, cnt1 = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
            #print(visited)
for i in range(n):
    for j in range(n):
        if graph[i][j] =='G':
            graph[i][j] = 'R'

visited = [[False ] * n for _ in range(n)] 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt1 += 1
print(cnt, cnt1)
