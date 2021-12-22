import sys
input = sys.stdin.readline

n = int(input())
x, y = 1, 1
mv = input().strip().replace(" ", "")
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for i in mv:
    print(x, y)
    m = 0
    if i == 'D':
        m = 3
    elif i == 'U':
        m = 2
    elif i == 'R':
        m = 0
    elif i == 'L':
        m = 1
    nx = direction[m][0] + x
    ny = direction[m][1] + y
    if nx > n or ny > n or ny < 1 or nx < 1:
        continue

    x, y = nx, ny

print(x, y)
