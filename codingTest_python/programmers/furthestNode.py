import heapq


def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)  # 1부터 떨어진 거리값 계산
    # graph edge 연결하기
    for i in edge:
        a, b = i
        graph[a].append([b, 1])
        graph[b].append([a, 1])

    # 최단 경로 계산
    def dijkstra(start):
        q = []
        heapq.heappush(q, [0, start])
        distance[start] = 0
        while q:
            dist, v = heapq.heappop(q)
            if distance[v] < dist:
                continue
            for i in graph[v]:
                cost = i[1] + dist
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, [cost, i[0]])
    dijkstra(1)
    maxV = max(distance[1:])
    for i in distance[1:]:
        if maxV == i:
            answer += 1

    return answer
