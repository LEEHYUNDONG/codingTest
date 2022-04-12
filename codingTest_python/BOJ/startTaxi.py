from collections import deque
import sys

input = sys.stdin.readline

N, M, gas = map(int, input().split())
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def findPass(graph, x, y):
    q = deque([])
    visited = [[-1]*N for _ in range(N)]
    q.append([x, y])
    visited[x][y] = 0
    minD = int(1e9)
    tmp = []
    while q:
        x, y = q.popleft()
        if visited[x][y] > minD:
            continue
        if [x, y] in start:
            minD = visited[x][y]
            tmp.append([x, y])
        for i in range(4):
            rx, ry = x + directions[i][0], y+directions[i][1]
            if 0 <= rx < N and 0 <= ry < N and visited[rx][ry] == -1:
                if graph[rx][ry] != 1:
                    visited[rx][ry] = visited[x][y]+1
                    q.append([rx, ry])
    if tmp:
        tmp.sort()
        return visited[tmp[0][0]][tmp[0][1]], tmp[0][0], tmp[0][1]
    else:
        return -1, -1, -1

def moveToDes(x, y, dest):
    q = deque([])
    q.append([x, y])
    visited = [[-1]*N for _ in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        if [x, y] == dest:
            return visited[x][y], x, y
        for i in range(4):
            rx, ry = x + directions[i][0], y+directions[i][1]
            if 0 <= rx < N and 0 <= ry < N and visited[rx][ry] == -1:
                if graph[rx][ry] != 1:
                    visited[rx][ry] = visited[x][y]+1
                    q.append([rx, ry])
    return -1, -1, -1
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())

start = []
dest = []

for i in range(M):
    a, b, c, d = map(int, input().split())
    dest.append([c-1, d-1])
    start.append([a-1, b-1])

tx -= 1
ty -= 1

for i in range(M):
    g, nx, ny = findPass(graph, tx, ty)   
    gas -= g
    if gas < 0 or g < 0:
        gas = -1
        break
    idx = start.index([nx, ny])
    start[idx] = [-1, -1]
    g, nx, ny = moveToDes(nx, ny, dest[idx])
    gas -= g
    dest[idx] = [-1, -1]
    if gas < 0 or g < 0:
        gas = -1
        break
    else:
        gas += 2*g
    tx, ty = nx, ny
    
        

print(gas)

