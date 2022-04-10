import sys
from collections import deque
input = sys.stdin.readline

directions = [
    (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
]

def moveBy(lst):
    q = deque(lst)
    tmp = []
    visited = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]
    for _ in range(len(q)):
        x, y, m, s, d = q.popleft()
        if m == 0:
            continue
        rx, ry = x, y
        for _ in range(s):
            rx += directions[d][0]
            ry += directions[d][1]
        rx %= N
        ry %= N
        if [rx, ry] not in tmp:
            tmp.append([rx, ry])
        if ((visited[2][rx][ry] % 2 == 1 or visited[0][rx][ry] == 0) and d % 2 == 1) or (visited[2][rx][ry] % 2 == 0 and d % 2 == 0):
            visited[2][rx][ry] = 1
        else:
            visited[2][rx][ry] = 0
        visited[2][rx][ry] += d 
        visited[0][rx][ry] += m
        visited[1][rx][ry] += s
        visited[3][rx][ry] += 1

    return visited, tmp

def fireBurst(lst):
    visited, lst = moveBy(lst)
    ttmp = []
    value = 0

    for i in range(len(lst)):
        rx, ry = lst[i]
        if visited[0][rx][ry]//5 == 0:
            continue
        if visited[3][rx][ry] <= 1:
            value += visited[0][rx][ry]
            ttmp.append([rx, ry, visited[0][rx][ry], visited[1][rx][ry], visited[2][rx][ry]])
            continue

        if visited[2][rx][ry] % 2:
            for i in range(4):
                ttmp.append([rx, ry, visited[0][rx][ry]//5, visited[1][rx][ry] // visited[3][rx][ry], 2*i])
        else:
            for i in range(4):
                ttmp.append([rx, ry, visited[0][rx][ry]//5, visited[1][rx][ry] // visited[3][rx][ry], 2*i+1])
            value += 4*(visited[0][rx][ry]//5)
    # print(ttmp)
    # for i in range(N):
    #     print(*visited[0][i])
    return ttmp, value


N, M, K = map(int, input().split())
attack = [list(map(int, input().split())) for _ in range(M)]
ans = 0


for _ in range(K):
    attack, ans = fireBurst(attack)

print(ans)
