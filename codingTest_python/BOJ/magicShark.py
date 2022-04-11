import sys
from collections import deque
input = sys.stdin.readline

directions = [
    (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
]

def moveBy(lst):
    q = deque(lst)
    visited = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(len(q)):
        x, y, m, s, d = q.popleft()
        rx, ry = x, y
        for _ in range(s):
            rx += directions[d][0]
            ry += directions[d][1]
        rx %= N
        ry %= N
        visited[rx][ry].append([m, s, d])

    return visited

def fireBurst(lst):
    visited = moveBy(lst)
    attack = []
    value = 0

    for i in range(N):
        for j in range(N):
            if len(visited[i][j]) > 1:
                M, S, ocnt, ecnt, cnt = 0, 0, 0, 0, len(visited[i][j])
                while visited[i][j]:
                    tmp = visited[i][j].pop(0)
                    M += tmp[0]
                    S += tmp[1]
                    if tmp[2] % 2:
                        ocnt += 1
                    else:
                        ecnt += 1
                if ocnt == cnt or ecnt == cnt:
                    if M // 5:
                        for k in range(4):
                            attack.append([i, j, M//5, S//cnt, 2*k])
                else:
                    if M // 5:
                        for k in range(4):
                            attack.append([i, j, M//5, S//cnt, 2*k+1])
            if len(visited[i][j]) == 1:
                attack.append([i, j] + visited[i][j].pop())

    return attack


N, M, K = map(int, input().split())
attack = [list(map(int, input().split())) for _ in range(M)]
ans = 0


for _ in range(K):
    attack = fireBurst(attack)

print(sum([i[2] for i in attack]))