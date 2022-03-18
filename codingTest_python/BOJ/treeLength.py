import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]].append([tmp[i+1], tmp[i]])


INF = int(1e9)
distance = [INF]*(n+1)
distance[0] = 0

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, x = heapq.heappop(q)
        if distance[x] < dist:
            continue
        for i in graph[x]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, [cost, i[1]])

dijkstra(1, distance)

distance2 = [INF]*(n+1)
distance2[0] = 0
idx = distance.index(max(distance))
dijkstra(idx, distance2)
print(max(distance2))

