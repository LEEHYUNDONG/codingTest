import heapq

n, k = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
graph = [[] for _ in range(n)]
distance = [INF]*(n)

for i in range(n):
    for j in range(n):
        if i != j:
            graph[i].append((j, planet[i][j]))

print(graph)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)
print(distance)



# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             planet[i][j] = min(planet[i][j], planet[i][k] + planet[k][j])
# print(planet)