import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
direction = [
    [[[0,1], [0, 1]], [[0, 1], [1, 1]]], # 가, 대
    [[[1, 0], [1, 0]], [[1, 0], [1, 1]]], # 세, 대
    [[[1, 1], [0, 1]], [[1, 1], [1, 0]], [[1, 1], [1, 1]]] # 가, 세, 대
    ] # 가로, 세로, 대각선

answer = 0
tail, head = [0, 0], [0, 1]
graph = [list(map(int, input().split())) for _ in range(n)]

def pipeLaid(tail, head):
    if head[0] - tail[0]  == 0 and head[1] - tail[1] == 1: # 가
        return 0
    elif head[0] - tail[0] == 1 and head[1] - tail[1] == 0: # 세
        return 1
    elif head[0] - tail[0]  == 1 and head[1] - tail[1] == 1: #대
        return 2

def inRange(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

q = deque([[head, tail]])

while q:
    h, t = q.popleft()
    hx, hy = h
    tx, ty = t
    # print(t, h)
    if h[0] == n-1 and h[1] == n-1:
        answer += 1
        continue
    shape = pipeLaid(t, h)
    for i in direction[shape]:
        hdx, hdy = hx+i[1][0], hy+i[1][1]
        tdx, tdy = tx+i[0][0], ty+i[0][1]
        if inRange(hdx, hdy) and inRange(tdx, tdy):
            if graph[hdx][hdy] == 1 or graph[tdx][tdy] == 1:
                continue
            if graph[hdx][hdy] == 0 and graph[tdx][tdy] == 0:
                newshape = pipeLaid([tdx, tdy], [hdx, hdy])
                if newshape == 2:
                    if graph[hdx-1][hdy] == 1 or graph[hdx][hdy-1] == 1:
                        continue
                q.append([[hdx, hdy], [tdx, tdy]])

    
print(answer)    