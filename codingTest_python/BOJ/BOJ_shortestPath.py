import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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

dijkstra(start)
for i in range(1, v+1):
    print("INF") if distance[i] == INF else print(distance[i])