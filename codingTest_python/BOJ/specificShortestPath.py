import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

INF = int(1e9)
distance = [INF]*(n+1)
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    res = []
    while q:
        dist, v = heapq.heappop(q)
        if dist > distance[v]:
            continue
        for i in graph[v]:
            cost = i[1] + dist
            if distance[i[0]] >= cost:
                heapq.heappush(q, [cost, i[0]])
                distance[i[0]] = cost
                res.append([v, i[0]])
    return distance

distance = [INF]*(n+1)
d1 = dijkstra(1)
distance = [INF]*(n+1)
dv1 = dijkstra(v1)
distance = [INF]*(n+1)
dv2 = dijkstra(v2)
ans = min(d1[v1] + dv1[v2] + dv2[n], d1[v2]+dv2[v1]+dv1[n])
if ans >= INF:
    print(-1)
else:
    print(ans)