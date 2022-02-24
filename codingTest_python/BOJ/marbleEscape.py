import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
red = []
blue = []
dest = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    tmp = input().strip()
    for j in range(m):
        if tmp[j] == 'R':
            red.extend([i, j])
        if tmp[j] == 'B':
            blue.extend([i, j])
        if tmp[j] == 'O':            
            dest.extend([i, j])
    graph.append(list(tmp))

graph[red[0]][red[1]] = '.'
graph[blue[0]][blue[1]] = '.'

def bfs():
    rq = deque([red])
    bq = deque([blue])
    res = 0
    while res < 10:
        res += 1
        for _ in range(len(rq)):
            x, y = rq.popleft()
            for rx, ry in direction:
                dx, dy = x + rx, y + ry
                if 0 <= dx < n and 0 <= dy < m:
                    if graph[dx][dy] == '#':
                        continue
                    if dx == dest[0] and dy == dest[1]:
                        return res
                    while graph[dx][dy] == '.':
                        dx += rx
                        dy += ry
                        if graph[dx][dy] == 'O':
                            return res
                    rq.append([dx-rx, dy-ry])
        
        for _ in range(len(bq)):
            x, y = bq.popleft()
            for rx, ry in direction:
                dx, dy = x + rx, y + ry
                if 0 <= dx < n and 0 <= dy < m:
                    if graph[dx][dy] == '#':
                        continue
                    if graph[dx][dy] == 'O':
                        return -1
                    while graph[dx][dy] == '.':
                        if graph[dx][dy] == 'O':
                            return -1
                        dx += rx
                        dy += ry
                    bq.append([dx-rx, dy-ry])
    return -1

print(bfs())