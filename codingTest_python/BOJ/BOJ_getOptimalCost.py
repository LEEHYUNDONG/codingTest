import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
a, b = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, v = heapq.heappop(q)
        if dist > distance[v]:
            continue
        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(a)
print(distance[b])