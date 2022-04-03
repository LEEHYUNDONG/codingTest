import sys
from collections import deque

input = sys.stdin.readline
max_size = 32768

t = int(input())

def bfs(startX, startY, store, px, py):
    q = deque([])
    q.append([startX, startY]) 

    while q:
        x, y = q.popleft()
        if abs(x-px) + abs(y-py) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = True
    
    return "sad"

for _ in range(t):
    n = int(input())
# 집, 편의점, 락 페스티벌 좌표
    startX, startY = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    px, py = map(int, input().split())
    visited = [False for _ in range(n+1)]
    print(bfs(startX, startY, store, px, py))