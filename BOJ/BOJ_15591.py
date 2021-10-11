import heapq

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(n-1):
    pi, qi, r = map(int, input().split())
    graph[pi].append((r, qi))
    graph[qi].append((r, pi))

res = []


def dijkstra(start, k):
    q = []
    cnt = 0
    path = []
    heapq.heappush(q, (k, start))
    visited[start] = True
    for i in graph[start]:
        visited[i[1]] = True
        q.append((i[0], i[1]))
    while q:
        cost, now = heapq.heappop(q)
        if cost >= k:
            cnt += 1
            for i in graph[now]:
                if not visited[i[1]]:
                    visited[i[1]] = True
                    q.append((min(cost, i[0]), i[1]))

    return cnt-1


for _ in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n+1)
    ans = dijkstra(v, k)
    res.append(ans)

for i in res:
    print(i)
