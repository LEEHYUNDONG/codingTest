import sys
import copy

input = sys.stdin.readline

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1),
                (1, 0), (1, 1), (0, 1), (-1, 1)]

graph = [[] for _ in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))
    
    for j in range(4):
        graph[i].append([tmp[2*j], tmp[2*j+1]-1])


def find(graph, idx):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == idx:
                return (i, j)
    return None

def moveAll(graph, now_x, now_y):
    for i in range(1, 17):
        loc = find(graph, i)
        if loc == None:
            continue
        x, y = loc
        turn = graph[x][y][1]
        for j in range(8):
            dx, dy = x + directions[turn][0], y + directions[turn][1]
            if 0 <= dx < 4 and 0 <= dy < 4:
                if not (dx == now_x and dy == now_y): # 상어가 없는 칸
                    graph[x][y], graph[dx][dy] = graph[dx][dy], graph[x][y]
                    graph[dx][dy][1] = turn
                    break
            turn = (turn+1)%8

def whereToEat(graph, x, y):
    pos = []
    to = graph[x][y][1]
    for i in range(1, 4):
        dx, dy = (x + directions[to][0]), (y + directions[to][1])
        if 0 <= dx < 4 and 0 <= dy < 4 and graph[dx][dy][0] != -1:
            pos.append([dx, dy])
        x, y = dx, dy
    return pos


def dfs(graph, x, y, tot):
    global answer
    graph = copy.deepcopy(graph)
    tmp = graph[x][y][0]
    graph[x][y][0] = -1
    moveAll(graph, x, y)
    res = whereToEat(graph, x, y)

    answer = max(answer, tot+tmp)

    for dx, dy in res:
        dfs(graph, dx, dy, tot+tmp)
    
answer = 0
dfs(graph, 0, 0, 0)
print(answer)

