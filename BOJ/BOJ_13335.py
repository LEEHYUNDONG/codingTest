import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
cnt = 0

if sum(truck) <= w:
    print(w+n)
else:
    l = []
    for i in range(n):
        for j in range(i):
            if sum(truck[j:i+1]) <= L:
                cnt += 1
                l.append(i-j+1)
    print((w+1)*n - w*(cnt+1))
