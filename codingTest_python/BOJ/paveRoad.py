import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    edges.append([a, b])

print(graph)

# distance = [INF]*(n+1)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, [0, start])
#     distance[start] = 0
#     while q:
#         dist, v = heapq.heappop(q)
#         if dist > distance[v]:
#             continue
#         for i in graph[v]:
#             cost = dist + i[0]
#             if distance[i[1]] >= cost:
#                 heapq.heappush(q, [cost, i[1]])            
#                 distance[i[1]] = cost

# distance = [INF]*(n+1)
# res = dijkstra(1)
# ans = INF

# # k개의 도로를 포장하는데 거리를 0으로 세팅할 수 있다. 모든 경우를 세팅해놓고 brute force 가능?