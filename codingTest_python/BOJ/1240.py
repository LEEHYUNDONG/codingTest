import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


for _ in range(M):
    a, b = map(int, input().split())
    ans = 0
    def bfs(start, end):
        q = deque()
        q.append(start)
        visit = [-1] * (N + 1)
        visit[start] = 0
        while q:
            cur = q.popleft()
            if cur == end: break
            for adj_node, adj_dist in graph[cur]:
                if visit[adj_node] > -1: continue
                visit[adj_node] = visit[cur] + adj_dist
                q.append(adj_node)
        return visit[end]
    print(bfs(a, b))

