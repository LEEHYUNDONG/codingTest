import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bomb = []

final = [['.' for _ in range(c)] for _ in range(r)]
data = []

for i in range(r):
    tmp = input().rstrip()
    for j in range(c):
        if tmp[j] == 'O':
            bomb.append([i, j])
    data.append(list(tmp))

cnt = 0
time = n
while cnt < time:
    if cnt % 3 == 0:
        cnt += 1
        continue
    elif cnt % 3 == 1:
        for i in range(r):
            for j in range(c):
                if data[i][j] != 'O':
                    new_bomb.append([i, j])
    elif cnt % 3 == 2:
        while bomb:
            x, y = bomb.popleft()

    cnt += 1
