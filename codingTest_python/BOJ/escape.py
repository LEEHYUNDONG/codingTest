import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
water = []
visited = [[0]*c for _ in range(r)]
startX, startY = 0, 0

for i in range(r):
    row = list(input().strip())
    for j in range(c):
        if row[j] == '*':
            water.append([i, j])
        elif row[j] == 'S':
            startX, startY = i, j
            visited[i][j] = 0
    graph.append(row)


# 물이 먼저 퍼지고 그 뒤에 도치가 움직인다고 생각하면 될듯? 
# 물이 한번 쭉 퍼지고 새로 들어온 물은 따로 저장
waterq = deque(water) # 물이 차오르는 큐
q = deque([[startX, startY]])
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = True


def bfs(startX, startY):
    q = deque([[startX, startY]])
    visited[startX][startY]= 0
    while q:
        for _ in range(len(waterq)):
            wx, wy = waterq.popleft()
            for rx, ry in direction:
                dwx, dwy = wx + rx, wy + ry
                if 0 <= dwx < r and 0 <= dwy < c:
                    # if not visited[dwx][dwy] and graph[dwx][dwy] != 'X' and graph[dwx][dwy] == '.' and graph[dwx][dwy] != '*':
                    if graph[dwx][dwy] == '.' and graph[dwx][dwy] != '*':
                        # tmp.append([dwx, dwy])
                        graph[dwx][dwy] = '*'
                        waterq.append([dwx, dwy])

        for _ in range(len(q)):
            x, y= q.popleft()
            for rx, ry in direction:
                dx, dy = x + rx, y + ry
                if 0 <= dx < r and 0 <= dy < c:
                    
                    if graph[dx][dy] == 'D':
                        return visited[x][y] + 1
                    if visited[dx][dy]:
                        continue
                    if graph[dx][dy] == '.':
                        visited[dx][dy] = visited[x][y] +1
                        q.append([dx, dy])
        
    return "KAKTUS"

print(bfs(startX, startY))