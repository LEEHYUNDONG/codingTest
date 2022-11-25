import sys
input = sys.stdin.readline
sys.setrecursionlimit(8000)

graph = [list(input().rstrip()) for _ in range(5)]
ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False]*5 for _ in range(5)]
tmp = []

def dfs(x, y, s, yy, depth):
    global ans
    if depth == 7 and s >= 4 and s > y:
        ans += 1
        return    
    for i in range(4):
        rx, ry = x + dx[i], y + dy[i]
        if 0 <= rx < 5 and 0<= ry < 5:
            if not visited[rx][ry] and graph[rx][ry] == 'S':
                dfs(x, y, s+1, yy, depth+1)
            elif not visited[rx][ry] and graph[rx][ry] == 'Y':
                dfs(x, y, s, yy+1, depth+1)

for i in range(5):
    for j in range(5):
        ttmp = []
        if graph[i][j] == 'S':
            dfs(i, j, 1, 0, 1)
        elif graph[i][j] == 'Y':
            dfs(i, j, 0, 1, 1)