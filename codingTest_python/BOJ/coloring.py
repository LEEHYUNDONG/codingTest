import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, N):
    q = deque([])
    x = 0
    for i in range(1, N+1):
        if len(graph[i]):
            x = i
            break
    
    q.append(x)
    visited = [0]*(N+1)
    visited[x] = 1
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] != 0 and visited[i] == visited[x]:
                return False
            if visited[i] == 0:
                visited[i] = visited[x]*-1
                q.append(i)
    return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if bfs(graph, N):
        print("possible")
    else:
        print("impossible")
    
    