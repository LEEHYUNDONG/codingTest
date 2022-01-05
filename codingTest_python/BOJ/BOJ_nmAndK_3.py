import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = -1000000
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, tot, depth):
    global ans
    if depth == k:
        ans = max(tot, ans)
        return
    for i in range(x, n):
        for j in range(y if x == i else 0, m):
            flag = True
            if visited[i][j]:
                continue
            for q in range(4):
                rx = i + dx[q]
                ry = j + dy[q]
                if 0 <= rx < n and 0 <= ry < m and visited[rx][ry]:
                    flag = False
                    break
            if flag:
                visited[i][j] = True
                dfs(i, j, tot+graph[i][j], depth+1)
                visited[i][j] = False


dfs(0, 0, 0, 0)
print(ans)
