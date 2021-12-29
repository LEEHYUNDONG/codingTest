from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque([[x, y, 1]])
    visited[x][y] = 1

    while q:
        x, y, c = q.popleft()
        if x == n-1 and y == m-1:
            print(c)

        for i in range(4):
            rx = dx[i] + x
            ry = dy[i] + y
            if 0 <= rx < n and 0 <= ry < m:
                if not visited[rx][ry] and graph[rx][ry] == '1':
                    q.append([rx, ry, c+1])
                    visited[rx][ry] = c+1


bfs(0, 0)
# print(visited[n-1][m-1])
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
