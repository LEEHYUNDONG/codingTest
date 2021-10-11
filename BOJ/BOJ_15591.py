import heapq

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(n-1):
    pi, qi, r = map(int, input().split())
    graph[pi].append((r, qi))
    graph[pi].append((r, pi))

res = []


def dijkstra(start, k):
    cnt = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        for i in graph[now]:
            if not visited[i[1]]:
                if i[0] >= k:
                    heapq.heappush(q, (i[1], i[0]))
                    visited[i[1]] = True
                    cnt += 1
    return cnt


for _ in range(q):
    k, v = map(int, input().split())
    q = []
    visited = [False] * (n+1)
    ans = dijkstra(v, k)
    res.append(ans)

print(res)
