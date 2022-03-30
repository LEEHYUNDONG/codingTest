import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([])
move = [-1 for _ in range(200001)]
visited = [int(1e9) for i in range(200001)]

q.append([n, 0])
move[n] = 0

ans = int(1e9)

while q:
    x, cnt = q.popleft()
    if x == k:
        ans = min(cnt, ans)

    if 2*x <= 100000 and move[2*x] == -1:
        q.appendleft([x*2, cnt+1])
        move[2*x] = x
    if 0 <= x-1 and move[x-1] == -1:
        q.append([x-1, cnt+1])
        move[x-1] = x
    if x+1 <= 100000 and move[x+1] == -1:
        q.append([x+1, cnt+1])
        move[x+1] = x


print(ans)
if n == k:
    print(n)
else:
    x = k
    tmp = [x]
    while move[x]:
        x = move[x]
        tmp.append(x)
    if n == 0:
        tmp.append(0)
    
    print(*tmp[::-1])