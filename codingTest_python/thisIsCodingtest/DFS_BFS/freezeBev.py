n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(graph, x, y, visited):

    for i in range(4):
        rx = dx[i] + x
        ry = dy[i] + y
        if 0 <= rx < n and 0 <= ry < m:
            if not visited[rx][ry] and graph[rx][ry] == '0':
                visited[rx][ry] = True
                dfs(graph, rx, ry, visited)
    return 1


ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == '0':
            visited[i][j] = True
            ans += dfs(graph, i, j, visited)

print(ans)
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
