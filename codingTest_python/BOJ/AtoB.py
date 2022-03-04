from collections import deque

a, b = map(int, input().split())

def solution():
    q = deque([])
    cnt = 1
    q.append([a, cnt])
    while q:
        v, cnt = q.popleft()
        if v == b:
            return cnt
    
        if int(str(v)+'1') <= b:
            q.append([int(str(v)+'1'), cnt+1])
        if v*2 <= b:
            q.append([v*2, cnt+1])
    return -1

print(solution())