import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, v, visited):
    visited[v] = True
    q = deque([[v, 0]])
    while q:
        item, d = q.popleft()
        for i in graph[item]:
            if not visited[i]:
                q.append([i, d+1])
                visited[i] = d+1


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    bfs(graph, i, visited)
    ans.append(sum(visited)-1)

print(ans.index(min(ans))+1)
