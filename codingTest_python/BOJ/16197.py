import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(N)]


def bfs(x, y):
    visited = [[False]*M for _ in range(N)]
    q = deque([])
    q.append(())
    
    while q:
        x, y, dist = q.popleft()
        

