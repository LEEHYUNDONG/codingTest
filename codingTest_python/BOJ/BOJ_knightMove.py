import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

move = [
    (-2, -1), (-1, -2), (1, -2), (-2, 1),
    (2, 1), (2, -1), (1, 2), (-1, 2)
]
ans = []

for _ in range(t):
    l = int(input())
    q = deque([])
    x, y = list(map(int, input().split()))
    destX, destY = list(map(int, input().split()))
    q.append((x, y, 0))
    visited = [[False] * l for _ in range(l)]
    visited[x][y] = True
    while q:
        x, y, c = q.popleft()
        if x == destX and y == destY:
            ans.append(c)
            break
        for dx, dy in move:
            rx, ry = x + dx, y+dy
            if 0 <= rx < l and 0 <= ry < l and not visited[rx][ry]:
                q.append((rx, ry, c+1))
                visited[rx][ry] = True

for i in ans:
    print(i)
