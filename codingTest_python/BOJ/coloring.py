import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, N):
    q = deque([])

    q.append(start)
    visited = [0]*(N+1)
    visited[start] = 1
    
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
    start = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        start = a
    if bfs(graph, start, N):
        print("possible")
    else:
        print("impossible")
    
    