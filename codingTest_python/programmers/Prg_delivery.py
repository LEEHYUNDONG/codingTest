import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N)]
    INF = int(1e9)
    distance = [INF]*(N)

    for i in road:
        graph[i[0]-1].append([i[1]-1, i[2]])
        graph[i[1]-1].append([i[0]-1, i[2]])

    q = []
    heapq.heappush(q, [0, 0])
    distance[0] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # print(distance)
    for i in distance:
        if i <= K:
            answer += 1
    return answer
