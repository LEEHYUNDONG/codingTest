import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bomb = []
data = []
new_bomb = []
final = [['.' for _ in range(c)]]*r

for i in range(r):
    tmp = input().rstrip()
    for j in range(c):
        if tmp[j] == 'O':
            bomb.append([i, j])
    data.append(list(tmp))

cnt = 0
time = n

# def allBombSet():
#     for i in range(r):
#         for j in range(c):


# def bfs(b):
#     q = deque(b)
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             rx, ry = x + dx[i], y + dy[i]
#             if 0 <= rx < r and 0 <= ry < c:
#                 if data[rx][ry] == '.':
#                     data[rx][ry] = 'O'


if n == 1:
    for i in range(r):
        print('O'*c)

elif n % 2 == 0:
    for i in range(r):
        print('O'*c)

elif n % 4 == 1 and n > 1:
    for i in range(r):
        for j in range(c):
            print(data[i][j], end='')
        print()

else:
    q = deque(bomb)
    while q:
        x, y = q.popleft()
        for i in range(4):
            rx, ry = x + dx[i], y + dy[i]
            if 0 <= rx < r and 0 <= ry < c:
                if data[rx][ry] == 'O':
                    data[rx][ry] = '.'

    for i in range(r):
        for j in range(c):
            if data[i][j] == '.':
                print("O", end='')
            else:
                print(".", end='')
        print()
