import sys
import heapq
input = sys.stdin.readline

a, b = map(int,input().split())
n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, v = heapq.heappop(q)
        if dist > distance[v]:
            continue
        for i in graph[v]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, [cost, i])


bfs(a)
print(-1) if distance[b] == INF else print(distance[b])