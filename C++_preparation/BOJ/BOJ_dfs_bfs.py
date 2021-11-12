import heapq
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([])
    visited[start] = True
    q.append(start)
    while q:
        x = q.pop()
        print(x, end=" ")
        for i in graph[x]:
            if not visited[i]:
                q.appendleft(i)
                visited[i] = True


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i+1].sort()
dfs(v)
print()
visited = [False for _ in range(n+1)]
bfs(v)
print()
