import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0]
item.extend(list(map(int, input().split())))

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]:
            continue
        for i in graph[x]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, [cost, i[1]])

ans = -1
for i in range(1, n+1):
    distance = [INF]*(n+1)
    dijkstra(i, distance)
    tmp = 0
    for j in range(1, n+1):
        if distance[j] <= m:
            tmp += item[j]
    ans = max(tmp, ans)

print(ans)