# 4시 13분
import sys
import copy
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

directions = [
    [], 
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
    [[0, 1, 2, 3]]
]
cameraNum = 0
c = []
def surveillance(x, y, direction, tmp):
    for i in direction:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[i], ny + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = -1
            else:
                break

answer = int(1e9)
def dfs(graph, cnt, c):
    global answer
    tmp = copy.deepcopy(graph)
    if cnt == cameraNum:
        c = 0
        for i in tmp:
            c += i.count(0)
        answer = min(answer, c)
        return
    x, y, cam = c[cnt]
    for i in directions[cam]:
        surveillance(x, y, i, tmp)
        dfs(tmp, cnt + 1, c)
        tmp = copy.deepcopy(graph)


for i in range(n):
    for j in range(m):
        if 1<= graph[i][j] <= 5:
            cameraNum += 1
            c.append([i, j, graph[i][j]])

dfs(graph, 0, c)
print(answer)